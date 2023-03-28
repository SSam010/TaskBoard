from django.urls import path, include

from .views import *


urlpatterns = [
    path('api/v1/', TaskApiList.as_view(), name='TaskApiList'),
    path('api/v1/<int:pk>/', TaskApiOne.as_view(), name='TaskApiDetail'),
    path('api/v1/create/', TaskApiCreate.as_view(), name='TaskApiCreate'),
    path('api/v1/update/<int:pk>/', TaskApiUpdate.as_view(), name="TasksApiUpdate"),
    path('api/v1/delete/<int:pk>/', TaskApiDelete.as_view(), name="TasksApiDelete"),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('', index),
]
