from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  RegisterUser, ToDoCreate, ToDoDelete, ToDoDetail, ToDoList, ToDoUpdate,  PhotoViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
# router.register(r'todos/viewset', ToDoViewSet, basename='todo')
router.register(r'photos', PhotoViewSet, basename='photo')

urlpatterns = [
    path('', include(router.urls)),
    path('todos/', ToDoList.as_view(), name='todo-list'),
    path('todos/create/', ToDoCreate.as_view(), name='todo-create'),
    path('todos/<int:pk>/', ToDoDetail.as_view(), name='todo-detail'),
    path('todos/update/<int:pk>/', ToDoUpdate.as_view(), name='todo-update'),
    path('todos/delete/<int:pk>/', ToDoDelete.as_view(), name='todo-delete'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

