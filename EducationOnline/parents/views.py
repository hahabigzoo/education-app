#-*- encoding=utf-8 -*-

'''
Created on 2019年6月6日

@author: yaachou
'''

import json
from cart.cart import Cart
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from parents.processing.processing import *


# Create your views here.
def index(request):      
    return HttpResponse('这是第一个测试请求回复！')


# 注册账号
def register(request):
    return render(request, 'register.html')


# 注册信息审核
def get_regi_info(request):
      
    # 获取注册表单信息
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    phone = request.POST['phone']
    validation_got = request.POST['validation']
    
    # 初始化错误提醒error_warning
    error_warning = []
    
    # 若无错误则注册，否则弹出错误信息
    if username_check(username)!=True:
        error_warning = [username_check(username)]
    elif password_check(password)!=True:
        error_warning = [password_check(password)]
    elif phone_check(phone)!=True:
        error_warning = [phone_check(phone)]
    else:
        validation = '1234'
        if validation_got == validation:
            try:
                Users.objects.create(username=username, password=password)
            except:        
                # 未知异常
                error_warning = ['抱歉，注册失败，请稍后重试...']
        else:
            error_warning = ['抱歉，验证码错误，请重试！']   
    if len(error_warning) == 0:
        return HttpResponse('注册成功！')
    else:
        return render(request, 'register.html', {'error_warning': json.dumps(error_warning)})


# 获取邮箱并发送验证码
def get_validation(request):
    
    # 判断是否为已登录状态
    if request.session.get('logined_user'):
        return HttpResponse('抱歉，您已登录，请先注销登录当前账户！')
    else:
        pass
    
    # 获取用户输入的邮箱
    email = request.GET['email']
    
    # 全局变量，便于调用
    global validation
    
    # 若为未绑定邮箱则提示
    try:
        user = Parents.objects.get(email = email)
    except Parents.DoesNotExist:
        return render(request, 'retrive.html', {'error': '抱歉，无此用户！'})    

    # 若为已绑定邮箱则发送邮件并记录验证码
    result = vali_email(email)
    if result:
        validation = result
        return render(request, 'password_reset.html', {'user': user})
    else:
        return render(request, 'get_validation.html', {'error': '抱歉，邮件发送失败，请稍后重试！'})


# 获取用户输入的验证码及新密码
def password_reset(request):
    
    # 判断是否为已登录状态
    if request.session.get('logined_user'):
        return HttpResponse('抱歉，您已登录，请先注销登录当前账户！')
    else:
        pass
    
    # 获取实际验证码用户输入的信息
    username = request.POST['username']
    got_validation = request.POST['validation']
    new_password = request.POST['new_password']
    reconfirm = request.POST['reconfirm']
    
    # 输入出错则提示
    if got_validation != validation:
        return render(request, 'password_reset.html', {'error': '抱歉，验证码输入错误，请检查邮件！'})
    elif new_password != reconfirm:
        return render(request, 'password_reset.html', {'error': '抱歉，两次密码输入不一致，请检查并重试！'})
    
    # 输入正确则更新数据库
    try:
        user = Users.objects.get(username = username)
    except Users.DoesNotExist:
        return render(request, 'password_reset.html', {'error': '抱歉，输入的用户名不存在，请检查重试'})
    finally:
        user.password = new_password
        user.save()
    return True


# 登录界面
def login(request):
    return render(request, 'login.html')


# 登录时检查（账号、密码正确则跳转主界面；否则输出错误信息！）
def login_check(request):
    
    # 获取登录表单信息
    username = request.POST['username']
    password = request.POST['password']
    
    # 若无错误则登录，否则弹出错误信息
    try:
        u = Users.objects.get(username = username)           
        if u.password == password:            
            # 已经登录，弹出“重复登录”提示信息
            if request.session.get('logined_user', ''):
                return HttpResponse('您已登录，不要重复登录！')           
            # 未登录，则建立session并跳转到主界面
            else:
                request.session['logined_user'] = username
                return render(request, 'index.html')       
        # 密码错误
        else:
            return HttpResponse('对不起，密码输入错误！')      
    except (UnboundLocalError, Users.DoesNotExist):
        # 用户不存在
        return HttpResponse('抱歉，该用户不存在！')
        

# 登录状态下展示用户信息
def display_info(request):
    username = request.session.get('logined_user', '')
    if request.method == 'POST':
        return HttpResponseNotFound('<h1>Page not found</h1>')
    elif username:
        user = Users.objects.get(username = username)
        user = user.parents_set.get(username = username)
        
        # 构建信息列表方便传到html
        info_list = [username, user.email, user.phone, user.name, user.balance ,user.child_name, user.child_age, user.child_sex]
        return render(request, 'display_info.html', {'info_list': info_list, 'username': username})
    else:
        return HttpResponse('请先登录！')


# 修改用户信息
def alter_info(request):
    
    # 获取当前登录用户
    username = request.session.get('logined_user')
    user = Parents.objects.get(username = username)
    
    # 获取用户信息表单内容
    email = request.POST['email']
    phone = request.POST['phone']
    name = request.POST['name']
    child_name = request.POST['child_name']
    child_age = request.POST['child_age']
    child_sex = request.POST['child_sex']
    
    # 更新数据库
    user.email = email
    user.phone = phone
    user.name = name
    user.child_name = child_name
    user.child_age = child_age
    user.child_sex = child_sex
    user.save()
    
    return redirect('../display_info/')


# 根据关键字查询课程信息
def seek_lessons(request):
    
    # 判断是否为已登录状态
    if request.session.get('logined_user'):
        pass
    else:
        return HttpResponse('抱歉，您还未登录，请先登录！')
    
    # 获取关键字和带有关键字的课程信息（若为空，则显示全部课程信息）
    keywords = request.GET['keywords']
    show_list = Lessons.objects.filter(name__icontains=keywords)
    
    return render(request, 'display_info.html', {'show_list': show_list})


# 申请试听
def apply_listening(request):
    
    # 判断是否为已登录状态
    username = request.session.get('logined_user')
    if username:
        pass
    else:
        return HttpResponse('抱歉，您还未登录，请先登录！')
    
    # 判断为申请试听（保存信息）还是取消试听（删除信息）并提示
    apply_listening = request.GET['apply_listening']
    if apply_listening:
        user = Parents.objects.get(username = username)
        user_name = user.name
        phone = user.phone
        return HttpResponse('已成功申请！')
    else:
        return HttpResponse('已取消申请！')


# 对试听效果做出评价
def comment(request):
    
    # 获取当前登录用户的用户名
    username = request.session.get('logined_user', '')
    
    # 判断是否为已登录状态
    if username:
        pass
    else:
        return HttpResponse('抱歉，您还未登录，请先登录！')
    
    # 获取表单评价内容
    stars = request.GET['stars']
    words = request.GET['words']
    images = request.GET['images']
    
    # 将评价存入数据库
    comment_item = Comments.objects.get(username = username)
    comment_item.stars = stars
    comment_item.words = words
    comment_item.images = images
    
    return

'''
# 加入购物车
def cart(request, goods_id, goods_list):
    
    # 判断是否为已登录状态
    if request.session.get('logined_user'):
        pass
    else:
        return HttpResponse('抱歉，您还未登录，请先登录！')
    
    # 创建购物车
    goods = Lessons.objects.get(goods_id = goods_id)
    # goods_list = list()
    goods_list += goods
    
    return goods_list
'''

# 展示课程信息
def display_lessons(request):
    return render(request, 'lessons_list.html')


# 添加到购物车（默认数量为一）
def add_to_cart(request, quantity=1):
    
    # 判断是否为已登录状态
    username = request.session.get('logined_user')
    if username:
        pass
    else:
        return HttpResponse('抱歉，您还未登录，请先登录！')
    
    # 添加到购物车
    lesson_id = request.GET['lesson_id']
    lesson = Lessons.objects.get(id=lesson_id)
    cart = Cart(request)
    cart.add(lesson, lesson.price, quantity)
    return redirect('../get_cart/')


# 根据课程id从购物车移除
def remove_from_cart(request):
    lesson_id = request.GET['lesson_id']
    lesson = Lessons.objects.get(id=lesson_id)
    cart = Cart(request)
    cart.remove(lesson)
    return redirect('../get_cart/')


# 获取购物车内容
def get_cart(request):
    
    # 判断是否为已登录状态
    username = request.session.get('logined_user')
    if username:
        pass
    else:
        return HttpResponse('抱歉，您还未登录，请先登录！')
    
    # 返回购物车内容
    return render(request, 'cart.html', {'cart': Cart(request)})


# 付款购买课程
def payment(request, cost):
    
    # 判断是否为已登录状态
    username = request.session.get('logined_user','')
    if request.session.get('logined_user'):
        pass
    else:
        return HttpResponse('抱歉，您还未登录，请先登录！')
    
    # 获取登录用户余额信息
    user = Parents.objects.get(username = username)
    balance = user.balance
    
    # 判断余额是否充足
    if balance > cost:
        balance -= sum
        return HttpResponse('付款成功！')
    else:
        return HttpResponse('抱歉，余额不足！\n请联系管理员进行充值（qq:123456789）')
    

# 注销登录
def logout(request):
    try:
        del request.session['username']
    except:
        return HttpResponse('抱歉，您还未登录！')
    finally:
        return HttpResponse('注销登录成功！')