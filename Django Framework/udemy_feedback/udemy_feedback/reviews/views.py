from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from udemy_feedback.reviews.forms import CreateReviewForm
from udemy_feedback.reviews.models import Review


def review(request):
    if request.method == 'POST':
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            review = Review(**form.cleaned_data)
            review.save()
            return redirect('thank-you')

    form = CreateReviewForm()
    context = {
        'form': form
    }
    return render(request, 'review.html', context)


def thanks(request):
    return render(request, 'thanks.html')
