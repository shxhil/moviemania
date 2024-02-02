from rest_framework import serializers
from django.contrib.auth.models import User
from apis.models import Movie,Genre,Profile,Review

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        fields=["username","email","password"]
        model=User
     #password encript akaan ahn ee methord introduce cheyyane (create_user)ahn posswordencript by overwriting default creat method  
    def create(self,validated_data):#validated data da akath ahn aa User vech input aakya ella detailsm,in set of tople format l
        return User.objects.create_user(**validated_data)


class MovieSerializer(serializers.ModelSerializer):
    genre=serializers.StringRelatedField(many=True)
    language=serializers.StringRelatedField(many=True)
    class Meta:
        model=Movie
        fields="__all__"
        read_only_fields=["id"]
        

class ProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        fields="__all__"
        model=Profile
        read_only_fields=["user","to_watch"]


class ReviewSerializer(serializers.ModelSerializer):
    movie=serializers.StringRelatedField()
    profile=serializers.StringRelatedField()
    class Meta:
        model=Review
        fields="__all__"
