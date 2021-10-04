import json

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Account
from django.views import generic
from django.contrib.auth.hashers import make_password

class SignUpView(View):
    def get(self, request):
        return render(request, 'account/signup.html')


    def post(self, request):
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        res_data = {}
        if not (username and email and password and re_password):
            res_data['error'] = 'empty value detected'
        elif Account.objects.filter(email = email).exists():
            res_data['error'] = 'exist email'

        elif password != re_password:
            res_data['error'] = 'different password'

        else:
            new_account = Account(
                email = email,
                password = make_password(password),
                username = username
            )
            new_account.save()
        return render(request, 'account/signup.html', res_data)

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
