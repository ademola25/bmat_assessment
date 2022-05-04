# Bmat Assessment

## Required Dependencies


**pip install -r requirements.txt**


## Setting the database

Create a Postgres database and copy my .env-example file and rename it with your db details in your .env file

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': os.getenv('DB_NAME'),
'USER': os.getenv('DB_USER'),
'PASSWORD': os.getenv('DB_PASSWORD'),
'HOST': os.getenv('DB_HOST'),
'PORT': os.getenv('DB_PORT', '5432'),
}
}

## Migrations, superuser and runserver

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python manage.py runserver



Importing metadata from a CSV file
------------------------------------

A custom django command was created to import metadata from a CSV file.


python manage.py import_metadata <path-to-file>



**Matching and Reconciling**
-----------------------------------

The logic is in `view.py`.Two separate function for them both`matching` and `reconcile_data`. I then used
`load_work()` function to Load the data into database after making sure it passes matching and Reconcile Requirements
  
  
### TO RUN TEST
 Run python manage.py test
  
  
## Questions Given for part1
-----------------------
1. Describe briefly the matching and reconciling method chosen.
Answer:
## Matching
Checking the db if incoming iswc_code exists or a metadata with the
same title and contributors exist. Here i use the Q object to acheive the comparison btw both
  
## Reconciling
we first iterate through the column and check if there is no
previous value for each of them , if not then update the column with the new value
I use `getattri()` function to check for value and use `setattri()` to update with new value

Then we iterate thru contributors and then perform a merge
 of db contributor and metadata contributor with extend function
 if the metadata.contributor is not in the db.

  
2. We constantly receive metadata from our providers, how would you automatize the process?
Using the bulk_create method should be considered

  
## Questions For part 2

1. Imagine that the Single View has 20 million musical works, do you think your solution would have a similar response time?
No it won't. Querying will take more much time with this current database size

2. If not, what would you do to improve it?
Optimization:
A great idea for improving the loading speed of a massive CSV would be to use `MULTI_PROCESSING`, In the command above, you could split the one big CSV file into multiple smaller files (the best approach would be to try to use indexes of rows) and put each batch of work under a separate process.  and ofcourse there is downside to this as well, you will need more free CPUs.
Also, writing `raw sql` optimized queries



