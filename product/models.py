from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import mark_safe
# Create your models here.
from django.db.models import Avg, Count
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.db.models.signals import pre_save
from mptt.fields import TreeForeignKey
from django.utils.text import slugify
from mptt.models import MPTTModel
# Create your models here.


class Project(models.Model):    
    Project_Type = (
        ('COMPLATE', 'COMPLATE'),
        ('ONGOING', 'ONGOING'),
        ('UPCOMING', 'UPCOMING'),
    )

    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=1255)
    description = models.TextField(max_length=1255)
    image=models.ImageField(upload_to='images/',null=False)
    detail=RichTextUploadingField()
    slug = models.SlugField(null=True,blank=True, unique=True,max_length=250)
    Project_Type=models.CharField(max_length=10,choices=Project_Type)
    featured_project = models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='2. Project'


    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Project ,self).save(*args , **kwargs)


    def get_absolute_url(self):
        return reverse('project_details', kwargs={'slug': self.slug})

    def avaregereview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
        avg=0
        if reviews["avarage"] is not None:
            avg=float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt=0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt

class Project_Images(models.Model):
    product=models.ForeignKey(Project,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

class Service(models.Model):    
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=1255)
    description = models.TextField(max_length=1255)
    image=models.ImageField(upload_to='images/',null=False)
    detail=RichTextUploadingField()
    aboutus = models.TextField(max_length=1255,null=True,blank=True)
    slug = models.SlugField(null=True,blank=True, unique=True,max_length=250)
    status=models.CharField(max_length=10,choices=STATUS)
    featured_project = models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='3. Service'


    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Service ,self).save(*args , **kwargs)


    def get_absolute_url(self):
        return reverse('service_details', kwargs={'slug': self.slug})

    def avaregereview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
        avg=0
        if reviews["avarage"] is not None:
            avg=float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt=0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt

class Service_Images(models.Model):
    product=models.ForeignKey(Service,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class Service_Key_Feature(models.Model):
    product = models.ForeignKey(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)  # changed
    description = models.CharField(max_length=100, blank=True, null=True)  # changed
    icon = models.CharField(max_length=50, blank=True, null=True)  # changed

    def __str__(self):
        return self.title
            



class Product(models.Model):    
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=1255)
    description = models.TextField(max_length=1255)
    usp_line = models.CharField(max_length=150,null=True,blank=True)
    image=models.ImageField(upload_to='images/',null=False,)
    detail=RichTextUploadingField()
    slug = models.SlugField(null=True,blank=True, unique=True,max_length=250)
    status=models.CharField(max_length=10,choices=STATUS)
    featured_project = models.BooleanField(default=False)
    Top_Deals_Of_The_Day = models.BooleanField(default=False)
    Top_Selling_Products = models.BooleanField(default=False)
    Recommended_For_You = models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='1. Product'


    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Product ,self).save(*args , **kwargs)


    def get_absolute_url(self):
        return reverse('product_details', kwargs={'slug': self.slug})

    def avaregereview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
        avg=0
        if reviews["avarage"] is not None:
            avg=float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt=0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt

class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name_plural='4. Comment'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']

