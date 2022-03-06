from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def mario_has_big_pp(request):
    return HttpResponse('Mario has big pishka')


def mario_lives_in_sofia(request, id):
    return HttpResponse(f'Mario is here in Sofia currently to make exam{id}')
