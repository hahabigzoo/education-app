from django.db import models

# Create your models here.
class Users( models.Model ):
    username = models.CharField( max_length=20 ,primary_key=True )
    password = models.CharField( max_length=20 )
    privilege = models.PositiveSmallIntegerField()
    audited =  models.BooleanField(default=True)
    ## 1 Admin,2 Agency ,3 Parent
