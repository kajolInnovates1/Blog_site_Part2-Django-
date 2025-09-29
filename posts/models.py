from django.db import models
from categories.models import Category
from authors.models import Author

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category= models.ManyToManyField(Category)
    #  many to many field mane holo aikhne many post er many category thakte pare abar many categoryry many post thakte pare that's why many many to relationship deta hoi

    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    # akta author er many post thakte pare but akta post er aktai author thakbe that's call many to one field so i used Foreign key 
    # when author deleter her profile then automaitcally delete his post that's why i used on_delete=models.CASECADE but we don't want to delete this post then i used models.Null this profile showing Null 
    def __str__(self):
        return self.title