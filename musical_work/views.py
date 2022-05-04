from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import Q


from musical_work.models import MusicalWork
from musical_work.serializers import MusicalWorkSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http.response import HttpResponse


from rest_framework import viewsets
import json
# Create your views here.



def matching(work_metadata):
    """
    Checking the db if incoming iswc_code exists or a metadata with the 
    same title and contributors exist.
    """
    
    return MusicalWork.objects.filter(
        Q(iswc=work_metadata['iswc']) |
        Q(title=work_metadata['title'], contributors=work_metadata['contributors'])
    ).first()
    


def reconcile_data(musical_work, work_metadata):
    """
    we first iterate through the column and check if there is no 
    previous value for each of them , if not then update the column with the new value
    
    Then we iterate thru contributors and then perform a merge
    of db contributor and metadata contributor with extend function
    if the metadata.contributor is not in the db.
    """
    columns = ['title', 'iswc']
    
    for column in columns:
        if not getattr(musical_work, column):
            setattr(musical_work, column, work_metadata[column])

    for contributor in work_metadata['contributors']:
        if contributor not in musical_work.contributors:
            musical_work.contributors.extend(contributor)
            musical_work.save()
    
    return musical_work


def load_work(work_metadata):
    """
    Loading the data into database after making sure. It doesn't already exist
    """
    musical_work = matching(work_metadata)
    if musical_work:
        #since it already exist, then update the musical_work to make it complete
        print("the metadata already exist")
        musical_work = reconcile_data(musical_work, work_metadata)
    else:
        #its a new musicl work so create new musical work to db
        musical_work = MusicalWork.objects.create(**work_metadata)
    return musical_work


class MusicalWorkViewset(viewsets.ModelViewSet):
    serializer_class = MusicalWorkSerializer

    def get_queryset(self): 
        musical_work = MusicalWork.objects.all()
        return musical_work
        
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        musical_work = MusicalWork.objects.filter(iswc=params['pk'])
        serializer = MusicalWorkSerializer(musical_work, many=True)
        return Response(serializer.data)
        
