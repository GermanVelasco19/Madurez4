from rest_framework import serializers
from Madurez40.models import Empresa


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empresa  
        exclude = ['is_removed', 'created', 'modified']

