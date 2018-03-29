# import django_filters
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.throttling import (
    AnonRateThrottle,
    UserRateThrottle,
)
from rest_framework import (
    authentication,
    permissions,
    viewsets,
    mixins
)
from .models import (
    Film,
    Person
)
from .serializers import (
    FilmSerializer,
    PersonSerializer,
    UserSerializer
)

UserModel = get_user_model()

class UserCreateView(APIView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class FilmViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

    queryset = Film.objects.available()
    serializer_class = FilmSerializer

    def list(self, request):
        queryset = self.get_queryset()
        if request.GET.get('name', None):
            queryset = queryset.filter(
                name__icontains=request.GET.get('title')
            )
        if request.GET.get('year', None):
            queryset = queryset.filter(
                year=request.GET.get('year')
            )

        serializer = self.serializer_class(
            queryset,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


class PersonViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):

    queryset = Person.objects.available()
    serializer_class = PersonSerializer

    def list(self, request):
        queryset = self.get_queryset()
        if request.GET.get('name', None):
            queryset = queryset.filter(
                Q(first_name__icontains=request.GET.get('name')) |
                Q(last_name__icontains=request.GET.get('name'))
            )
        if request.GET.get('alias', None):
            queryset = queryset.filter(
                alias__icontains=request.GET.get('alias')
            )

        serializer = self.serializer_class(
            queryset,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
