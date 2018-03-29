from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import (
    Film,
    Person
)

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=UserModel.objects.all())]
    )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password')


class FilmBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'year',)


class FilmSerializer(serializers.ModelSerializer):
    casting = serializers.SerializerMethodField()
    director = serializers.SerializerMethodField()
    producer = serializers.SerializerMethodField()

    def get_casting(self, obj):
        return PersonBasicSerializer(
            obj.as_actor.all(),
            many=True
        ).data


    def get_director(self, obj):
        return PersonBasicSerializer(
            obj.as_director.all(),
            many=True
        ).data


    def get_producer(self, obj):
        return PersonBasicSerializer(
            obj.as_producer.all(),
            many=True
        ).data



    class Meta:
        model = Film
        fields = ('id',
                  'title', 'year',
                  'casting', 'director', 'producer')


class PersonBasicSerializer(serializers.ModelSerializer):
    aliases = serializers.SerializerMethodField()

    def get_aliases(self, obj):
        return obj.aliases()


    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'aliases', )



class PersonSerializer(serializers.ModelSerializer):
    aliases = serializers.SerializerMethodField()
    actor = serializers.SerializerMethodField()
    director = serializers.SerializerMethodField()
    producer = serializers.SerializerMethodField()

    def get_aliases(self, obj):
        return obj.aliases()

    def get_actor(self, obj):
        return FilmBasicSerializer(
            obj.as_actor.all(),
            many=True
        ).data

    def get_director(self, obj):
        return FilmBasicSerializer(
            obj.as_director.all(),
            many=True
        ).data

    def get_producer(self, obj):
        return FilmBasicSerializer(
            obj.as_producer.all(),
            many=True
        ).data



    class Meta:
        model = Person
        fields = ('id',
                  'first_name', 'last_name', 'aliases',
                  'actor', 'director', 'producer'
        )
