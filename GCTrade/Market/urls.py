from django.urls import path
from .views import GC_BuyView, GC_SellView

app_name = 'Market'
urlpatterns = [
    path('Buy/', GC_BuyView.as_view()),
    path('Sell/', GC_SellView.as_view()),
    # path('/logout', views.Logout, name='logout'),
]


