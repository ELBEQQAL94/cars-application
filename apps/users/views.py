import json

from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

#from apps.submissions.models import StudentSubmission
#from apps.projects.models import Project
from .models import UserProfile
#from .permissions import ObjectPermission


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'is_seller')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        is_seller = validated_data.pop('is_seller')
        user = get_user_model().objects.create_user(**validated_data)
        user.is_seller = is_seller
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
                queryset=get_user_model().objects.all())

    class Meta:
        model = UserProfile
        fields = ('__all__')


class CreateUserSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
                queryset=get_user_model().objects.all())

    class Meta:
        model = UserProfile
        fields = ('__all__')


# @permission_classes([IsAuthenticated])
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    # def list(self, request, *args, **kwargs):
    #     raise PermissionDenied()


# @permission_classes([IsAuthenticated])
class UserProfileView(APIView):
    def get(self, request, pk):
        profile = UserProfile.objects.get(user=pk)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request, pk):
        # name, bio, github_username, avatar, current_level
        profile = UserProfile(
            **request.data
        )
        profile.user = get_user_model().objects.get(pk=pk)
        profile.save()
        
        return Response('Success')


