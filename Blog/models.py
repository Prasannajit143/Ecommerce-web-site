from django.db import models

# Create your models here.

class blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,default ="")
    post_date = models.DateTimeField()
    author = models.CharField(max_length=15,default ="")
    content = models.CharField(max_length=5000,default ="")
    title_subhead_1 = models.CharField(max_length=50,default ="")
    content_subhead_1 = models.CharField(max_length=5000,default ="")
    title_subhead_2 = models.CharField(max_length=50,default ="")
    content_subhead_2 = models.CharField(max_length=5000,default ="")
    thumbnail = models.ImageField(upload_to="Blog/images",default ="")
    about = models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.title

