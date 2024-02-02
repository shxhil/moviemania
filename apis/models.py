from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save

from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.
class Genre(models.Model):
    name=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class Movie(models.Model):
    title=models.CharField(max_length=200)
    release_date=models.DateField()
    description=models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    genre=models.ManyToManyField(Genre)
    language=models.ManyToManyField(Language)
    poster=models.FileField(upload_to="movie_poster",default="default_poster")
    


    def  __str__(self) -> str:
        return self.title
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    to_watch=models.ManyToManyField(Movie,related_name="towatch")
    profile_pic=models.FileField(upload_to="profile",default="default_profile.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    options=(("male","male"),("female","female"))
    gender=models.CharField(max_length=200,choices=options,default="male")

    def  __str__(self) -> str:
        return self.user.username
    

    
class Review(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,related_name="movie_name")
    profile=models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile_name")
    rating=models.PositiveIntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def  __str__(self) -> str:
       return f"{self.profile.username} - {self.movie.title} - {self.rating}"
    
       
def create_profile(sender,created,instance,**kwargs):
    if created and not instance.is_superuser:
        Profile.objects.create(user=instance)

post_save.connect(create_profile,sender=User)