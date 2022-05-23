from django.urls import path
from .views import Create, List

urlpatterns = [
    path('create', Create.as_view()),
    path('', List.as_view()),
]
