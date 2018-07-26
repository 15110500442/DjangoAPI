from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tutorial.quickstart.models import Students

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class StudentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Students
        fields = ('name', 'sex', 'age', 'birthday', 'id_code', 'phone', 'email', 'native_place', 'address', 'hobby',
                  'enrollment_time')
