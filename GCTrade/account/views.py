import json

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Account
from django.views import generic


class SignUpView(View):
    def get(self, request):
        return render(request, 'account/signup.html')


    def post(self, request):
        data = json.loads(request.body)
        
        if Account.objects.filter(email = data['email']).exists():
            return HttpResponse(status=400)

        if data['password'] != data['confirm']:
            return HttpResponse(status=404)

        Account.objects.create(
           email = data['email'],
           password = data['password']
           )
        return JsonResponse({'message': '회원가입 성공'},status=200)


class SignInView(View):
    def get(self, request):
        return render(request, 'account/login.html')
        
    def post(self, request):
        data = json.loads(request.body)

        if Account.objects.filter(email = data['email']).exists() :
            user = Account.objects.get(email = data['email'])
            if user.password == data['password'] :
                return JsonResponse({'message':f'{user.email}님 로그인 되셨습니다.'}, status=200)
            else :
                return JsonResponse({'message':'비밀번호가 틀렸어요'},status = 401)

        return JsonResponse({'message':'미등록 이메일 입니다.'},status=400)

# def Logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         return redirect('/')

#     return render(request, 'login.html')



# Create your views here.
