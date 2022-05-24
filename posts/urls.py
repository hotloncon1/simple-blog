from django.urls import path
from .views import PostList,PostDetail,ListCreatePostAPIView, RetrieveUpdateDestroyPostAPIView

urlpatterns = [
    # path('<int:pk>/', PostDetail.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyPostAPIView.as_view()),
    # path('', PostList.as_view()),
    path('', ListCreatePostAPIView.as_view()),
]
