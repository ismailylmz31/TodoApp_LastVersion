from rest_framework import viewsets, status,generics, filters,permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import ToDo, Photo
from .serializers import ToDoSerializer,PhotoSerializer,UserSerializer
from rest_framework.views import APIView
import django_filters.rest_framework
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class LoginUser(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         return Response({'error': 'Invalid Credentials'}, status=400)




# class ToDoViewSet(viewsets.ModelViewSet):
#    serializer_class = ToDoSerializer
#    permission_classes = [IsAuthenticated]

#    def get_queryset(self):
#         return ToDo.objects.filter(user=self.request.user)

#    def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Photo.objects.filter(todo__user=self.request.user)
    

# Create
class ToDoCreate(generics.CreateAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
# Read (List)
class ToDoList(generics.ListAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['completed']
    search_fields = ['title']

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)

# Read (Detail)
class ToDoDetail(generics.RetrieveAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)

# Update
class ToDoUpdate(generics.UpdateAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)

# Delete
class ToDoDelete(generics.DestroyAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)




# # Create
# class ToDoCreate(APIView):
#     def post(self, request, format=None):
#         serializer = ToDoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Read (List)
# class ToDoList(APIView):
#     def get(self, request, format=None):
#         todos = ToDo.objects.all()
#         serializer = ToDoSerializer(todos, many=True)
#         return Response(serializer.data)

# # Read (Detail)
# class ToDoDetail(APIView):
#     def get(self, request, pk, format=None):
#         try:
#             todo = ToDo.objects.get(pk=pk)
#         except ToDo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         serializer = ToDoSerializer(todo)
#         return Response(serializer.data)

# # Update
# class ToDoUpdate(APIView):
#     def put(self, request, pk, format=None):
#         try:
#             todo = ToDo.objects.get(pk=pk)
#         except ToDo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = ToDoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Delete
# class ToDoDelete(APIView):
#     def delete(self, request, pk, format=None):
#         try:
#             todo = ToDo.objects.get(pk=pk)
#         except ToDo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)