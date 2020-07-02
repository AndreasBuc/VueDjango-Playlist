from rest_framework.serializers import ModelSerializer
from users.models import CustomUser


class UserDisplaySerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'id']
