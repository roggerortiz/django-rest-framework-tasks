from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.authentication import TokenAuthentication
from .serializers import TaskSerializer
from .models import Task


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
