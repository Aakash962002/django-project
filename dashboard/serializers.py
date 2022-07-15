from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import CrudOpr

class CrudSerializers(serializers.ModelSerializer):
    class Meta:
        model = CrudOpr
        fields = '__all__'
