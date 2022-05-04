
from django.db.models import Q
from bmat_assessment.musical_work.models import MusicalWork


def matching(work_metadata):
    """
    Checking the db if incoming iswc_code exists or a metadata with the 
    same title and contributors exist.
    """
    matched = MusicalWork.objects.filter(
        Q(iswc=work_metadata['iswc']) |
        Q(title=work_metadata['title'], contributors=work_metadata['contributors'])
    ).first()
    return matched


def reconcile_data(musical_work, work_metadata):
    """
    we first iterate through the column and check if there is no 
    previous value for the , if not then update the column with the new value
    we first check if there is no previous data value for the column
    """
    columns = ['title', 'iswc']
    
    for column in columns:
        if not getattr(musical_work, column):
            setattr(musical_work, column, work_metadata[column])


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

   
   #  /Users/mac/Desktop/bmat_assessment/bmat_assessment/works_metadata.csv