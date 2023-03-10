from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Review, VideoGame


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )

        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")


class VideoGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGame
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["comment", "star_rating", "location", "video_game", "user"]
        # read_only_fields = ('user',)

    # def create(self, validated_data):
    #     print(validated_data)
    #     print(validated_data["user"].id)
    #     return Review.objects.create(**validated_data)
    #     # import pudb;
    #     # pudb.set_trace()
    #     # return super().create(validated_data)
