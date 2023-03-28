from rest_framework import serializers

from .models import Tasks


class TasksApiSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Tasks
        fields = "__all__"
