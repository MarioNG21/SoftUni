from django.urls import path

from udemy_feedback.reviews.views import review

urlpatterns = [
    path('', review, name='review'),
]