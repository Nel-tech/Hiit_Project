from django.db import models

# Create your models here.
class contactMessage(models.Model):
    name =models.CharField(max_length=100)
    email =models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    image =models.ImageField(upload_to='images/', default="profile.jpg",blank=True,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
   

    def _str_(self):
      return self.subject