from rest_framework import serializers
from users.models import NewUser


class RegisterUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ('email','user_name','password')
        extra_kwargs = {'password':{'write_only':True}}
    
    

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instances = self.Meta.model(**validated_data)
        if password is not None:
            instances.set_password(password)
        instances.save()
        return instances
