import csv                                                                                                                              
import argparse
from musical_work.views import load_work
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
     help = "Load metadata from the CSV file."

     def add_arguments(self, parser):
         parser.add_argument('file', nargs='?', type=str, help='A file with the metadata')

     def handle(self, *args, **options):
         file_path = options['file']
         try:
             with open(file_path, 'r') as csv_file:
                 data = csv.reader(csv_file, delimiter=",")
                 next(data)
                 for row in data:
                     load_work({
                         'title':row[0],
                         'contributors':row[1].split('|'),
                         'iswc':row[2],
                     })
                 
         except Exception as e:
                
                raise CommandError('Csv file "%s" does not exist' % file_path)

         self.stdout.write(self.style.SUCCESS('Successfully imported data from "%s"' % file_path))