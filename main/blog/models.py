from datetime import date
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    id: int = models.AutoField(primary_key=True)
    publish_date: models.DateField = models.DateField(auto_now=True, db_column="PublishDate")
    text: str = models.CharField(max_length=1500, db_column="PublishDate")
    post_rating: float = models.FloatField(db_column="PostRating", null=True)
    number_of_ratings: int = models.IntegerField(db_column='NumberOfRatings', null=True)
    title: str = models.CharField(max_length=500, db_column="Title")
    user: User = models.ForeignKey(User, db_column='User', on_delete=models.CASCADE)



