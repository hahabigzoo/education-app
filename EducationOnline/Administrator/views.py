from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django import forms
from util import Util


# Create your views here.
class AgencyIndex(View):
    '''首页'''

    def get(self, request):
        util = Util()
        username = util.check_user(request)
        if username == '':  ##未登录
            return
        else:
            return  ##已登录

    def post(self, request):
        pass


class AgencyLogin(View):
    '''教育机构登陆,注册界面，如果存在账户则登陆，不存在则跳转到注册界面'''

    def post(self, request):
        uf = forms.Form(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            if username == '' or password == '':
                return render(request, "AgencyLogin.html", {'uf': uf, "error": "用户名和密码不能为空"})
            ## 判断用户名与密码是否匹配
            pass
            if user:  ##登陆成功
                response = HttpResponseRedirect('/agency/index/')
                request.session['username'] = username  # 将session信息写到服务器
                return response
            else:
                return render(request, "AgencyLogin.html", {'uf': uf, "error": "用户名或密码错误"})


class AgencyLogout(Views):
    # 用户登出
    def get(request):
        response = HttpResponseRedirect('/index/')  # 登出后跳转到首页
        request.session['username'] = ""
        return response

    def post(request):
        self.get(request)


class AgencyRegister(View):
    # 用户注册
    def post(self, request):
        ## 用户提交注册表单
        uf = forms.Form(request)
        if uf.is_valid():
            username = (request.POST.get('username')).strip()
            password = (request.POST.get('password')).strip()
            contact = (request.POST.get('contact')).strip()
            field = (request.POST.get('field')).strip()
            idcode = (request.POST.get('idecode')).strip()
            address = (request.POST.get('address')).strip()




