import json
from os import name

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Actor, ActorMovie, Movie


class ActorView(View):
    def post(self, request):
        data = json.loads(request.body)
        Actor.objects.create(
            first_name = data["first_name"],
            last_name = data["last_name"],
            date_of_birth = data["date_of_birth"]
        )
        return JsonResponse({"message" : "SUCCESS"}, status=201)


    def get(self, request):
        actors = Actor.objects.all()
        
        result = []
        for actor in actors:
        
            result.append(
                {
                    "배우" : actor.last_name + actor.first_name,
                    "영화목록" : [actor_movie.movie_id.title for actor_movie in actor.actormovie_set.all()]
                }
            )
        

        return JsonResponse({"actors" : result}, status=200)

class MovieView(View):
    def post(self, request):
        data = json.loads(request.body)
        Movie.objects.create(
            title = data["title"],
            release_date = data["release_date"],
            running_time = data["running_time"]
        )
        return JsonResponse({"message" : "SUCCESS"}, status=201)


    def get(self, request):
        movies = Movie.objects.all()
        result = []
        for movie in movies:
            result.append(
                {
                    "영화제목" : movie.title,
                    "상영시간" : movie.running_time,
                    "출연배우" : [movie_actor.actor_id.last_name + movie_actor.actor_id.first_name for movie_actor in movie.actormovie_set.all()]
                    
                }
            )
        

        return JsonResponse({"movies" : result}, status=200)


class ActorMovieView(View):
    def post(self, request):
        data = json.loads(request.body)
        ActorMovie.objects.create(
            # actor_id = input_data["actor_id"],
            # movie_id = input_data["movie_id"]
            actor_id = Actor.objects.get(id=data["actor_id"]),
            movie_id = Movie.objects.get(id=data["movie_id"])

        )

        return JsonResponse({"message" : "SUCCESS"}, status=201)


    def get(self, request):
        '''
        actormovies = ActorMovie.objects.all()
        result = []
        movie_list = []

        for actormovie in actormovies:
            for movies in actormovie:
                movie_list.append({
                    "movie_list" : movies.movie_id.title
                })

            result.append({
                "first_name" : actormovie.actor_id.first_name,
                "last_name" : actormovie.actor_id.last_name,
                "movie_list" : movie_list

            })
    
        '''

        return #JsonResponse({"actormovies" : result}, status=200)

