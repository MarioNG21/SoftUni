from django.urls import path

from employee_app.mario.views import mario_has_big_pp, mario_lives_in_sofia

urlpatterns = [
    path('', mario_has_big_pp),
    path('<path:id>/', mario_lives_in_sofia)
]
