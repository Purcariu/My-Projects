from rest_framework import serializers 
from Persons.models import Person
 
 
class PersonSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Person
        fields = ('id',
                  'first_name',
                  'last_name')
