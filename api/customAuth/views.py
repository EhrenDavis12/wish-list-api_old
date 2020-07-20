from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
# Create your views here.

# ReadOnlyModelViewSet
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # http_method_names = ['get', 'patch', 'post']