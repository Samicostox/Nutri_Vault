from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, PhysicSerializer, PreferencesSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User, Physic, Preferences

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
            
        
        return Response({
            'msg' : 'tu est nul'
        })


class RegisterPhysicView(APIView):
    def post(self,request):
        # make it impossible for users to have mutliple physic
        s = PhysicSerializer(data=request.data)
        if s.is_valid() :
            s.save()

           
            
            return Response({
                'Physic' : s.data
                
                
                })
            
        
        return Response({
            'msg' : 'tu est nul'
        })


    def get(self,request):
        
        user = User.objects.filter(pk=2).first()
        s = UserSerializer(user)
        physic = Physic.objects.filter(user=2).first()
        s2 = PhysicSerializer(physic)

        return Response({
            'user' : s.data,
            'physic' : s2.data
            })

class PrefView(APIView):
    def post(self,request):
        s = PreferencesSerializer(data = request.data)
        if s.is_valid() :
            s.save()
            return Response(s.data)



class UserView(APIView):
    def post(self,request):
        user_id = request.data['user_id']
        user = User.objects.filter(pk=user_id).first()
        s = UserSerializer(user)

        physic = Physic.objects.filter(user=user_id).first()
        s2 = PhysicSerializer(physic)

        preferences = Preferences.objects.filter(user=user_id).first()
        s3 = PreferencesSerializer(preferences)

        list = [s.data,s2.data,s3.data]

        return Response(list)




