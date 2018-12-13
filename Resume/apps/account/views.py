from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView


class LoginView(APIView):
    def post(self,request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
            #
            else:
                # Return an 'invalid login' error message.
                print(username)
                print(password)
                data = {
                    "LoninStatus": 0
                }
                return JsonResponse(data)

    def get(self, request):
        print(request.path)
        return JsonResponse("hello",safe=False)
