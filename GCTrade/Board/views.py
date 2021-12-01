from django.shortcuts import render, redirect

from django.views import View


class FreeTalkView(View):
    def get(self, request):
        return render(request, 'Board/FreeTalk.html')


    def post(self, request):
        return render(request, 'Board/FreeTalk.html')
