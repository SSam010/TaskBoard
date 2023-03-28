from django.urls import path, include

from .views import *


urlpatterns = [
    path('', TaskApiList.as_view(), name='TaskApiList'),
    path('<int:pk>/', TaskApiOne.as_view(), name='TaskApiDetail'),
    path('create/', TaskApiCreate.as_view(), name='TaskApiCreate'),
    path('update/<int:pk>/', TaskApiUpdate.as_view(), name="TasksApiUpdate"),
    path('delete/<int:pk>/', TaskApiDelete.as_view(), name="TasksApiDelete"),
    path('auth/', include('rest_framework.urls')),
]
