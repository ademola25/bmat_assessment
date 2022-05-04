from rest_framework import serializers

from .models import MusicalWork


class MusicalWorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = MusicalWork
        fields = ['id','title','contributors', 'iswc']
        #depth = 1