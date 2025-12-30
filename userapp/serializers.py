from rest_framework import serializers

from userapp.models import User,JobModel

class Userregisterserializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ['username','password','email']

    def create(slef,validated_data):

        user = User.objects.create_user(
            username = validated_data['username'],
            password=validated_data['password'],
            email = validated_data['email']
        )

        return user
    
class Jobserializer(serializers.ModelSerializer):

    class Meta:

        model = JobModel

        exclude = ('user',)