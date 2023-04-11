from django.db import models
# Create your models here.
class indexmail(models.Model):
    email=models.EmailField(max_length=200,null=True)
    # user = models.OneToOneField(User, null=True)

    def __str__(self):
        return self.email
    
class detailmail1(models.Model):
    name=models.CharField(max_length=200,null=True)
    email1=models.EmailField(max_length=200,null=True)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    person=models.CharField(max_length=300,null=True)
    def __str__(self):
        return self.email
    