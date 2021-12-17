
from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "password2",
            "country",
            "bio",
            "phone_number",
            "area_of_interest",
            "user_document",
            "birthday",
            "home_address",
            "office_address",
        )

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError({"password": "Passwords didn't match."})
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            country=validated_data["country"],
            bio=validated_data["bio"],
            phone_number=validated_data["phone_number"],
            area_of_interest=validated_data["area_of_interest"],
            user_document=validated_data["user_document"],
            birthday=validated_data["birthday"],
            home_address=validated_data["home_address"],
            office_address=validated_data["office_address"],
        )
       
        user.set_password(validated_data["password"])
        user.save()

        return user



class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "country",
            "bio",
            "phone_number",
            "area_of_interest",
            "user_document",
            "birthday",
            "home_address",
            "office_address",
        )