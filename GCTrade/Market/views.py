from django.shortcuts import render, redirect
from django.views import View

class GC_BuyView(View):
    def get(self, request):
        return render(request, 'Market/Buy.html')


    def post(self, request):
        return render(request, 'Market/Buy.html')

class GC_SellView(View):
    def get(self, request):
        return render(request, 'Market/Sell.html')


    def post(self, request):
        return render(request, 'Market/Sell.html')