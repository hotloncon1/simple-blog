from django.urls import path
from .views import Register, Login, List

urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('list', List.as_view()),
]
