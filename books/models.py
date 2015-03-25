from django.db import models
from editorial.models import Editorial
from authors.models import Author

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    book_file = models.FileField(upload_to='media/books')

    editorial = models.ForeignKey(Editorial)
    author = models.ForeignKey(Author)

    def __unicode__(self):
        return self.title
