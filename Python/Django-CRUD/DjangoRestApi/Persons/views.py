from django.shortcuts import render

from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Person
from Persons.serializers import PersonSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def person_list(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        persons_serializer = PersonSerializer(persons, many=True)
        response = JsonResponse(persons_serializer.data, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        return response

    elif request.method == 'POST':
        person_data = JSONParser().parse(request)
        person_serializer = PersonSerializer(data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse(person_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Person.objects.all().delete()
        return JsonResponse({'message': '{} Persons were deleted successfully!'.format(count[0])}, status=200)


@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, id):
    try:
        person = Person.objects.get(pk=id) 
    except Person.DoesNotExist: 
        return JsonResponse({'message': 'The person does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        person_serializer = PersonSerializer(person)
        return JsonResponse(person_serializer.data) 

    elif request.method == 'PUT':
        person_data = JSONParser().parse(request) 
        person_serializer = PersonSerializer(person, data=person_data)
        if person_serializer.is_valid(): 
            person_serializer.save() 
            return JsonResponse(person_serializer.data) 
        return JsonResponse(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        person.delete()
        
        return JsonResponse({'message': 'Person was deleted successfully!'}, status=200)