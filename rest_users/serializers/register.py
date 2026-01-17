from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "bio")
        read_only_fields = ("id",)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate(self, attrs):
        if attrs["password"].isdigit():
            raise serializers.ValidationError({
                "password": "Password cannot be numeric only"
            })
        return attrs

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            bio=validated_data.get("bio", ""),
            birth_date= validated_data.get("birth_date", None)
        )
        user.set_password(validated_data["password"])
        user.save()
        return user