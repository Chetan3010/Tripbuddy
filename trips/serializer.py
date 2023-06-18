from rest_framework import serializers
from trips.models import *

class TripsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = trips
        fields = "__all__"