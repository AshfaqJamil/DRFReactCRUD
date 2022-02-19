from django.shortcuts import get_object_or_404
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission,IsAuthenticated,DjangoModelPermissions
from rest_framework import viewsets
from rest_framework.response import Response
# Creating a custom permission for the auther of a post to update,delete his/her post
class PostUserWritePermission(BasePermission):
    message = 'Editing posts in restricted to the user only.'

    def has_object_permission(self, request, view, obj):
        if request.method is SAFE_METHODS:
            return True

        return obj.author == request.user

class PostList(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class = PostSerializer
    
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')


    def get_queryset(self):
        return Post.objects.all()

# class PostList(viewsets.ViewSet):
#     permission_classes=[IsAuthenticated]
#     queryset = Post.objects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset,pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)  


# class PostList(generics.ListCreateAPIView,):
#     permission_classes = [IsAuthenticatedOrReadOnly] #Restricting access to admin users only
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
