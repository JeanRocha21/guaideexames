from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Exame
from .serializers import ExameSerializer



class ExameViewSet(viewsets.ModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer


class pesquisa(ListView):
    template_name = "pesquisa.html"
    model = Exame

    def get_queryset(self):
        Busca = self.request.GET.get('query')

        if Busca:
            object_list = Exame.objects.filter(Nome__icontains=Busca)
            return object_list
        else:
            return None



class Homepage(ListView):
    template_name = "homepage.html"
    model = Exame

    def get_queryset(self):
        Busca = self.request.GET.get('query')

        if Busca:
            object_list = Exame.objects.filter(Nome__icontains=Busca)
            return object_list
        else:
            return None
