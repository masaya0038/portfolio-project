from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(max_length=10)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


#Create A Blog models

#Add the Blog to the settings

# Create a migration

# Migrate

# Add to the admin
