from rest_framework import serializers
import re
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'bio', 'user']

    def validate_name(self, value):
        if re.search(r'\d', value):
            raise serializers.ValidationError("Name cannot contain numbers.")
        return value

    def validate_email(self, value):
        if "gmail" not in value.lower():
            raise serializers.ValidationError("Email must contain 'gmail'.")
        return value
