from django.urls import path


from obshtak_exercise.monthly_challenges.views import monthly_challenge, monthly_challenge_by_number, list_of_months

urlpatterns = [
    path('', list_of_months, name='list_of_months'),
    path('<int:month>/', monthly_challenge_by_number, name='month_by_number'),
    path('<str:month>/', monthly_challenge, name='month_by_name')
]
