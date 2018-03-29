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

class CommaSeparatedField(serializers.Field):
    def to_representation(self, obj):
        return map(lambda a: a.strip(), obj.split(','))

    def to_internal_value(self, data):
        return data


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=UserModel.objects.all())]
    )
    password = serializers.CharField(min_length=8, write_only=True)

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
            obj.as_actor.available(),
            many=True
        ).data


    def get_director(self, obj):
        return PersonBasicSerializer(
            obj.as_director.available(),
            many=True
        ).data


    def get_producer(self, obj):
        return PersonBasicSerializer(
            obj.as_producer.available(),
            many=True
        ).data


    def create(self, validated_data):
        return Film.objects.create(
            title=validated_data.get('title', None),
            year=validated_data.get('year', None)
        )

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.year = validated_data.get('code', instance.year)
        instance.save()

        return instance

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
    alias = CommaSeparatedField()
    actor = serializers.SerializerMethodField()
    director = serializers.SerializerMethodField()
    producer = serializers.SerializerMethodField()


    def get_actor(self, obj):
        return FilmBasicSerializer(
            obj.as_actor.available(),
            many=True
        ).data

    def get_director(self, obj):
        return FilmBasicSerializer(
            obj.as_director.available(),
            many=True
        ).data

    def get_producer(self, obj):
        return FilmBasicSerializer(
            obj.as_producer.available(),
            many=True
        ).data


    def create(self, validated_data):
        print (validated_data)
        return Person.objects.create(
            first_name=validated_data.get('first_name', None),
            last_name=validated_data.get('last_name', None),
            alias=validated_data.get('alias', None),
        )

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.alias = validated_data.get('alias', instance.alias)
        instance.save()

        return instance


    class Meta:
        model = Person
        fields = ('id',
                  'first_name', 'last_name', 'alias',
                  'actor', 'director', 'producer'
        )
