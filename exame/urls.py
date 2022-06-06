from django.urls import path
from .views import ExameViewSet, Homepage, pesquisa

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('exames', ExameViewSet)

app_name = 'exame'

urlpatterns = [
    path('', pesquisa.as_view(), name="pesquisa"),
    path('homepage', Homepage.as_view(), name="homepage"),

    ]

