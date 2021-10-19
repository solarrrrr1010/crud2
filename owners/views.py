import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Owner, Dog

class OwnerView(View):
    def get(self, request):
        # 클라이언트의 요청을 처리할 수 있는 로직 작성
        Owner.objects.get(
            name=["name"], 
            email=["email"],
            age=["age"]
            )        
        return JsonResponse({"message" : "SUCCESS"}, status=200)

    def post(self, request):
        input_data = json.loads(request.body)
        Owner.objects.create(
            name=input_data["name"], 
            email=input_data["email"],
            age=input_data["age"]
            )

        return JsonResponse({"message" : "SUCCESS"}, status=201)


class DogView(View):
    def get(self, request):
        # 클라이언트의 요청을 처리할 수 있는 로직 작성
        Dog.objects.get(
    
                )
                
        
        
        return JsonResponse({"message" : "SUCCESS"}, status=200)

    def post(self, request):
        input_data = json.loads(request.body)
        Dog.objects.create(
            name=input_data["name"],
            age=input_data["age"],
            owner_id=input_data["owner_id"]
        )

        return JsonResponse({"message" : "SUCCESS"}, status=201)
        