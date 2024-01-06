# Imports
from rest_framework import serializers
from .models import*



#  URLshortner serializer
class Urlshotserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = URLShortener
        fields = ["id","long_url","short_url","created_at","no_of_count"]
