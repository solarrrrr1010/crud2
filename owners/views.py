import json
from os import name

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Owner, Dog

class OwnerView(View):
    def get(self, request):
        # 클라이언트의 요청을 처리할 수 있는 로직 작성
        owners = Owner.objects.all()
        result = []
        
        
        for owner in owners:
            dogs = list(Dog.objects.filter(owner=owner).values("name", "age")) #owner.dog_set.all()
            #dogs_list = []
            #for dog in dogs:
            #    dogs_list.append(
            #        {
            #            "name" : dog.name,
            #            "age" : dog.age
            #        }
            #    )


            result.append(
                {
                    "name" : owner.name,
                    "email" : owner.email,
                    "age" : owner.age,
                    "dog" : dogs #dogs_list
                }
            )
               
        return JsonResponse({"owners" : result}, status=200)

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
        dogs = Dog.objects.all()
        

        result = []
        for dog in dogs:
            result.append(
                {
                    "name" : dog.name,
                    "age" : dog.age,
                    "owner" : dog.owner.name
            
                }
                
            )
         
        return JsonResponse({"dogs" : result}, status=200)

    def post(self, request):
        input_data = json.loads(request.body)
        Dog.objects.create(
            name=input_data["name"],
            age=input_data["age"],
            owner_id=input_data["owner_id"]
            # owner = input_data.objects.get["owner_id"] 
            # >> post 할 때도 owner_id에 숫자 말고 이름을 직접 넣어줘야 한다.
        )

        return JsonResponse({"message" : "SUCCESS"}, status=201)
        
