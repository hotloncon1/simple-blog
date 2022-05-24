from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from .serializers import PostSerializer
from .models import Post
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .pagination import CustomPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.

class PostList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination

    def get(self, request):
        posts = Post.objects.all()
        data = PostSerializer(posts, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.user)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]
    """
       Retrieve, update or delete a post instance.
    """

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListCreatePostAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        # Assign the user who created the post
        serializer.save(owner=self.request.user)


class RetrieveUpdateDestroyPostAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

