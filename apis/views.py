from django.shortcuts import render
from apis.serializers import SignUpSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from apis.serializers import MovieSerializer,ProfileSerializer,ReviewSerializer
from apis.models import Movie,Profile,Review

from rest_framework import authentication,permissions
from rest_framework import serializers

from rest_framework.decorators import action
# Create your views here.

class SignUpView(APIView):

    def post(self,request,*args,**kwargs):
        deserializer=SignUpSerializer(data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(data=deserializer.data)
        else:
            return Response(data=deserializer.errors)
        
class MovieView(viewsets.ModelViewSet):
    serializer_class=MovieSerializer
    queryset=Movie.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):
        movie_obj=self.get_object()
        # movie_obj=Movie.objects.get(id=kwargs.get("pk"))
        user_obj=request.user
        
        id=int(kwargs.get("pk"))#movie id
        usergiven_reviewsid=request.user.profile_name.all().values_list("movie",flat=True)
        if id in usergiven_reviewsid:
            raise serializers.ValidationError("already existed")
        else:

            
            deserializer=ReviewSerializer(data=request.data)
            if deserializer.is_valid():
                deserializer.save(movie=movie_obj,profile=user_obj)
                return Response(data=deserializer.data)
            else:
                return Response(data=deserializer.errors)
        
    
    def create(self, request, *args, **kwargs)ghg:
        raise serializers.ValidationError("permission denied")
    
    def update(self, request, *args, **kwargs):
        raise serializers.ValidationError("permission denied")
    
    def destroy(self, request, *args, **kwargs):
        raise serializers.ValidationError("permission denied")

class ProfileViewset(viewsets.ModelViewSet):
    serializer_class=ProfileSerializer
    queryset=Profile.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


class ReviewView(viewsets.ViewSet):
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        r_obj=Review.objects.get(id=id)
        if request.user.id == r_obj.profile.id:
            serializer=ReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response (data=serializer.data)
            else:
                return Response (data=serializer.errors)
            
        else:
            raise serializers.ValidationError("permission needed")


# class ReviewViewet(viewsets.ModelViewSet):
#     serializer_class=ReviewSerializer
#     queryset=Review.objects.all()
#     authentication_classes=[authentication.TokenAuthentication]
#     permission_classes=[permissions.IsAuthenticated]

#     def list(self, request, *args, **kwargs): #to list only current login nned users s reviews only
#         id = request.user.id
#         reviews = Review.objects.filter(profile=id)
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(data=serializer.data)



#     def perform_update(self, serializer):
#         id= self.request.user.id
#         reviews= self.get_object()
#         print(reviews)
#         if id == reviews.profile.id:
#             return super().perform_update(serializer)
#         else:
#             raise serializers.ValidationError("user permission required")

#     # def perform_update(self, serializer):
#     #     if self.get_object().profile.id == self.request.user.id:
#     #         return super().perform_update(serializer)
#     #     else:
#     #         raise serializers.ValidationError("user permission required")
    
#     # def perform_destroy(self, instance):
#     #     if self.get_object().profile.id == self.request.user.id:
#     #         return super().perform_destroy(instance)
#     #     else:
#     #         raise serializers.ValidationError("user permission required")


#     def destroy(self, request, *args, **kwargs):
#         id=self.request.user.id
#         return super().destroy(request, *args, **kwargs)   