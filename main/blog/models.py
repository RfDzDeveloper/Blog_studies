from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    id: int = models.AutoField(primary_key=True)
    publish_date: models.DateField = models.DateField(auto_now=True, db_column="PublishDate")
    text: str = models.CharField(max_length=1500, db_column="Text")
    post_rating: float = models.FloatField(db_column="PostRating", null=True)    
    title: str = models.CharField(max_length=500, db_column="Title")
    user: models.ForeignKey = models.ForeignKey(User, db_column='User', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    id: int = models.AutoField(primary_key=True)
    publish_date: models.DateField = models.DateField(auto_now=True, db_column="PublishDate")
    text: str = models.CharField(max_length=500, db_column="Text")
    user: models.ForeignKey = models.ForeignKey(User, db_column='User', on_delete=models.DO_NOTHING)
    post: models.ForeignKey = models.ForeignKey(Post, db_column='Post', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.text

class EmailToken(models.Model):
    id = models.AutoField(primary_key = True)   
    token = models.CharField(max_length=100, db_column='Token', unique=True)
    email = models.CharField(max_length=100, db_column='Email')
    create_date = models.DateField(auto_now=True)

class UserRatings(models.Model):
    id = models.AutoField(primary_key=True)
    ratings: models.PositiveBigIntegerField = models.PositiveSmallIntegerField(
        db_column='Ratings', null=True)
    user: models.ForeignKey = models.ForeignKey(
        User, db_column='User', on_delete=models.DO_NOTHING, db_index=True)
    post: models.ForeignKey = models.ForeignKey(Post, db_column='Post', 
                                                on_delete=models.CASCADE, db_index=True)
    