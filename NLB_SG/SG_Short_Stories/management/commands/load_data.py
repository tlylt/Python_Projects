#2 after creating model, load csv data
from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from SG_Short_Stories.models import Book

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from data.csv into our model"

    def handle(self, *args, **options):
        if Book.objects.exists():
            print('Data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return

        print("Loading data")
        for row in DictReader(open('./national-library-board-read-short-story.csv')):
            book = Book()
            book.title = row['book_title']
            book.summary = row['summary']
            book.author = row['author_name']
            raw_date = row['published']
            published_year = datetime.strptime(raw_date, '%Y')
            book.publish_year = published_year
            book.download_link = row['resource_url']
            book.language = row['language']
            book.save()

