from django.db import models

# Create your models here.
# crate a blog model
# title
#pub_date
#body
#image

#Add the blog app in settings
#create migrate 
#add to the admin

class Blog(models.Model):
    title=models.CharField(max_length=50)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')


