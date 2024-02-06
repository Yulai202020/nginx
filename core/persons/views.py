from django.http import HttpResponse
from persons.models import Persons

def all_persons(request):
    person_ = Persons.objects.all()
    return HttpResponse(person_)

def by_id(request, person_id):
    person_ = Persons.objects.get(pk=person_id)
    return HttpResponse(person_)

def create(request, name, surname):
    person_ = Persons.objects.create(name = name, surname = surname)
    return HttpResponse(person_)

def delete(request, person_id):
    person_ = Persons.objects.filter(id=person_id).delete()
    return HttpResponse(person_)