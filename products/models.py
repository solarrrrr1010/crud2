from django.db import models
from django.db import DatabaseError
from django.db.models.deletion import CASCADE


class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    # 장고 공식 문서 확인 >> 데이터필드는 이렇게 비워두면 원래 안 됨!!!!!!

    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()
    # 장고 공식 문서 확인 >> 데이터필드는 이렇게 비워두면 원래 안 됨!!!!!!

    class Meta:
        db_table = 'movies'


class ActorMovie(models.Model):
    actor_id = models.ForeignKey('Actor', on_delete=models.CASCADE) 
    movie_id = models.ForeignKey('Movie', on_delete=models.CASCADE)

    class Meta:
        db_table = 'actors_movies'




