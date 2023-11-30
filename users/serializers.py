from rest_framework import serializers


from .models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    is_superuser = serializers.BooleanField( read_only=True)
    password = serializers.CharField(write_only=True)
    username = serializers.CharField() 
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(default=False)

    def validate_email(self, value):
        value = value.lower()
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("email already registered.")
        
        return value
    def validate_username(self, value):
        value=value.lower()
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("username already taken.")
        
        return value

    def create(self, validated_data):
        if validated_data["is_employee"]:
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)

        return user
    
    def update(self, instance: User, validated_data: dict):
        
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
       
        instance.save()

        return instance