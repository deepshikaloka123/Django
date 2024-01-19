from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .serializers import *
from .models import *

class customersignup(APIView):
    def post(self,request):
        try:

            serializer=customersignupserializer(data=request.data)
            if serializer.is_valid():
                username = serializer.data["username"]
                mobile = serializer.data["mobile"]
                email = serializer.data["email"]
                password = serializer.data["password"]

                customerData.objects.create(
                username=username,
                mobile=mobile,
                email=email,
                password=password
                )

                profile.objects.create(
                username_id=username,
                mobile=mobile,
                email=email,
                password=password
                )
                message = {"message": "customer signup successful"}
                return JsonResponse(message,status=status.HTTP_201_CREATED,safe=False)
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST,safe=False)
        except Exception as e:
            message={"message":str(e)}
            return JsonResponse(message,status=status.HTTP_400_BAD_REQUEST)

class customerlogin(APIView):
    def post(self,request):
        try:
            serializer=customerloginserializer(data=request.data)
            if serializer.is_valid():
                username=serializer.data["username"]
                password=serializer.data["password"]
                loginData=list(customerData.objects.filter(
                    username=username,password=password).values())
                if len(loginData) == 1:
                    message={"message":"login successful"}
                    return JsonResponse(message,status=status.HTTP_200_OK)
                else:
                    message = {"message": "invalid credentails"}
                    return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            message = {"message": str(e)}
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)

class getProfile(APIView):
    def get(self,request,username):
        try:
            profiledata = list(profile.objects.filter(username_id=username).values())
            return JsonResponse(profiledata, status=status.HTTP_200_OK,safe=False)


        except Exception as e:
            message = {"message": str(e)}
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)

class updateProfile(APIView):
    def put(self,request):
        try:
            serializer=updateProfileSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.data["username"]
                profile.objects.filter(username_id =username).update(
                    **serializer.data
                )
                message={"Message":"profile updated successfully"}
                return JsonResponse(message,status=status.HTTP_200_OK,safe=False)
            return JsonResponse(serializer.errors,status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            message = {"message": str(e)}
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)

class deleteCustomer(APIView):
    def delete(self,request,username):
        try:
            customerData.objects.filter(username=username).delete()
            message={"message":"customer deleted successfully"}
            return  JsonResponse(message,status=status.HTTP_204_NO_CONTENT,safe=False)
        except Exception as e:
            message = {"message":str(e)}
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)



