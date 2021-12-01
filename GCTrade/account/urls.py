from django.urls import path
from .views import SignInView, SignUpView, UserInfoView

app_name = 'account'
urlpatterns = [
    path('login/', SignInView.as_view()),
    # path('/logout', views.Logout, name='logout'),
    path('signup/', SignUpView.as_view()),
    path('UserInfo/', UserInfoView.as_view()),
]


