from django.db import models

# Create your models here.
class ApplyForm_a( models.Model ):
    username = models.CharField( max_length=30  )  ##username varchar(30) not null,
    field = models.CharField( max_length=100 )    ##field varchar(100) not null,
    idcode = models.CharField( max_length=30 )    ##idcode varchar(30) not null,
    address = models.CharField( max_length=100 , null=True  )  ##address varchar(100) ,
    contact = models.CharField( length=13 )       ##contact varchar(13) not null,
class ApplyForm_t( models.Model ):
    username = models.CharField( max_length=30  )  ##username varchar(30) not null,
    name = models.CharField( max_length=30 )    ##field varchar(30) not null,
    sex = models.CharField( max_length=1 )      ##
    age =models.PositiveSmallIntegerField()    ##

    

