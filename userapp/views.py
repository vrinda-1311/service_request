from django.shortcuts import render

from rest_framework.views import APIView

from userapp.models import User,JobModel

from userapp.serializers import Userregisterserializer,Jobserializer

from rest_framework.response import Response

from rest_framework import status

from rest_framework.permissions import AllowAny,IsAuthenticated

from rest_framework.authentication import BasicAuthentication,TokenAuthentication

from django.shortcuts import get_object_or_404

from rest_framework.authtoken.models import Token


# Create your views here.

class UserregisterView(APIView):

    permission_classes = [AllowAny]

    def post(self,request):

        user_serializer = Userregisterserializer(data= request.data)

        if user_serializer.is_valid():

            user = user_serializer.save()

            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Login(APIView):

    permission_classes = [IsAuthenticated]

    authentication_classes = [BasicAuthentication]

    def post(self,request):

        user = request.user

        token,created = Token.objects.get_or_create(user = request.user)

        return Response({"message":"login successfuly","token":token.key},status=status.HTTP_200_OK)
    
class Jobadd(APIView):

    permission_classes= [IsAuthenticated]

    authentication_classes = [TokenAuthentication]

    def post(self,request):

        serializer = Jobserializer(data = request.data)

        if serializer.is_valid():

            serializer.save(user=request.user)

            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):

        data = JobModel.objects.filter(user=request.user)

        serializer = Jobserializer(data,many = True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
class Jobupdatedeleteretrive(APIView):

    authentication_classes = [TokenAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self,request,**kwargs):

        id = kwargs.get('pk')

        job = get_object_or_404(JobModel,id = id,user = request.user)

        serializer = Jobserializer(job,many = False)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,**kwargs):

        id = kwargs.get('pk')

        dataa = get_object_or_404(JobModel,id = id,user = request.user)

        serializer = Jobserializer(dataa,data = request.data)

        if serializer.is_valid():
            
            serializer.save()

            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
            
            



    


