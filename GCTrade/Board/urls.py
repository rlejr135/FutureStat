from django.urls import path
from .views import FreeTalkView

app_name = 'Board'
urlpatterns = [
    path('FreeTalk/', FreeTalkView.as_view()),
    # path('/logout', views.Logout, name='logout'),
]


