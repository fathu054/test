from django.db import models

# Create your models here.

class Published(models.Model) :
    pb_img = models.ImageField(upload_to='publishedImages')
  
class Count(models.Model):
    ct_onl =models.CharField(max_length=12)
    ct_trt =models.CharField(max_length=12)
    ct_art =models.CharField(max_length=12)
    ct_essay =models.CharField(max_length=12)

class Articles(models.Model) :
    art_heading = models.CharField(max_length=100)
    art_name = models.CharField(max_length=50)
    art_para = models.TextField()
    art_id = models.AutoField(primary_key=True)

class Generalpage(models.Model):
    gn_heading = models.CharField(max_length=100)
    gn_name = models.CharField(max_length=50)
    gn_para = models.TextField()

class Propheticpage(models.Model):
    pr_heading = models.CharField(max_length=100)
    pr_name = models.CharField(max_length=50)
    pr_para = models.TextField()

class Socialpage(models.Model):
    sc_heading = models.CharField(max_length=100)
    sc_name = models.CharField(max_length=50)
    sc_para = models.TextField()
 
class Spiritualpage(models.Model):
    sp_heading = models.CharField(max_length=100)
    sp_name = models.CharField(max_length=50)
    sp_para = models.TextField()    
class Featured(models.Model):
    ft_id = models.AutoField(primary_key=True)
    ft_featureImage =models.ImageField(upload_to='Featured')
    ft_heading = models.CharField(max_length=100)
    ft_para = models.TextField()
    ft_coating = models.TextField()
    ft_authername = models.CharField(max_length=25)
    
