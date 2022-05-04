from rest_framework.test import APITestCase
from musical_work.models import MusicalWork
from rest_framework import status





class MusicalWorkTestCase(APITestCase):
    def setUp(self):
        self.musical_work = MusicalWork.objects.create(
            title='first case',
            contributors=['Contibutor one', 'Contibutor two'],
            iswc='T234567890',
        )
        self.musical_work_sample2 = MusicalWork.objects.create(
            title='second case ',
            contributors= ['Contibutor one', 'Contibutor two', 'Contibutor three'],
            iswc='T234567890',
        )
        self.musical_work_sample3 = MusicalWork.objects.create(
            title='third case ',
            contributors=['Contibutor one', 'Contibutor two', 'Contibutor three'],
            iswc='T8379369494',
        )
        
        self.musical_work_json = {
            'pk': str(self.musical_work.pk),
            'title':'first case',
            'contributors':['Contibutor one', 'Contibutor two'],
            'iswc':'T234567890',
        }
        self.musical_work_json2 = {
            'pk': str(self.musical_work_sample2.pk),
            'title':'third case',
            'contributors': ['Contibutor one', 'Contibutor two', 'Contibutor three'],
            'iswc': 'T234567890',
        }
        

    def test_retrieve_musical_works(self):
        response = self.client.get('/lookup/%s/' % str(self.musical_work.pk))

        assert response.json() == self.musical_work_json


    def test_list_musical_works(self):
        response = self.client.get('/lookup')
        assert response.json() == [self.musical_work_json, self.musical_work_json2]
        
        # Create your tests here.
 