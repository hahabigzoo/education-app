# from django.db import models
#
# # Create your models here.
# class Users( models.Model ):
#     username = models.CharField( max_length=20 ,primary_key=True )
#     password = models.CharField( max_length=20 )
#     privilege = models.PositiveSmallIntegerField()
#     audited =  models.BooleanField(default=True)
#     ## 1 Admin,2 Agency ,3 Parent
#
# class News( models.Model ):
#     title = models.CharField( max_length=30 ,primary_key=True )
#     contend = models.CharField( max_length=10000)
#     time = models.DateTimeField(auto_now=True)
#     photo=models.ImageField()
#
# class Video(models.Model):
#     STATUS_CHOICES = (
#         ('0', '发布中'),
#         ('1', '未发布'),
#     )
#     title = models.CharField(max_length=100,blank=True, null=True)
#     desc = models.CharField(max_length=255,blank=True, null=True)
#     file = models.FileField(max_length=255)
#     cover = models.ImageField(upload_to='cover/',blank=True, null=True)
#     status = models.CharField(max_length=1 ,choices=STATUS_CHOICES, blank=True, null=True)
#     create_time = models.DateTimeField(auto_now_add=True, blank=True, max_length=20)
#
#
from chunked_upload.models import ChunkedUpload
from django.db import models

# Create your models here.
class MyChunkedUpload(ChunkedUpload):
    pass
# Override the default ChunkedUpload to make the `user` field nullable
MyChunkedUpload._meta.get_field('user').null = True


