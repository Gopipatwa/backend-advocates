from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100,unique=True)
    logo = models.ImageField(upload_to = "company_logo")
    summary = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # what will be displayed in the admin
        return self.name


class Advocates(models.Model):
    name = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to="advocate_profile",blank=True,null=True)
    short_bio = models.CharField(max_length=250)
    long_bio = models.TextField(blank=True)
    advocate_years_exp = models.IntegerField(default=0)
    company = models.ForeignKey(Company,to_field="name",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # what will be displayed in the admin
        return self.name

class SocialLink(models.Model):
    advocate_id = models.ForeignKey(Advocates,on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=100)
    link = models.URLField()