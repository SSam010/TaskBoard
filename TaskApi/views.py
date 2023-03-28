from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Tasks
from .permissions import *
from .serializers import TasksApiSerializer


class TaskApiList(generics.ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksApiSerializer
    permission_classes = (IsAuthenticated,)


class TaskApiOne(generics.RetrieveAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksApiSerializer
    permission_classes = (IsAuthenticated,)


class TaskApiCreate(generics.CreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksApiSerializer
    permission_classes = (IsAuthenticated,)


class TaskApiUpdate(generics.UpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksApiSerializer
    permission_classes = (OwnerAndStaff,)


class TaskApiDelete(generics.DestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksApiSerializer
    permission_classes = (OwnerAndStaff,)
