from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from obshtak_exercise.monthly_challenges.models import Month

monthly_challenges = {
    'january': 'Eat no meat for the entire month',
    'february': 'Walk for at least 20 min every day',
    'march': 'Learn Django every day for 3 hours',
    'april': 'Eat no meat for the entire month',
    'may': 'Walk for at least 20 min every day',
    'june': 'Learn Django every day for 3 hours',
    'july': 'Eat no meat for the entire month',
    'august': 'Walk for at least 20 min every day',
    'september': 'Learn Django every day for 3 hours',
    'october': 'Eat no meat for the entire month',
    'november': 'Walk for at least 20 min every day',
    'december': None,
}


def monthly_challenge_by_number(request, month):
    moths = list(monthly_challenges.keys())
    if month < len(moths):
        forward_month = moths[month]
        return redirect(to='month_by_name', month=forward_month)
    else:
        return Http404()


def monthly_challenge(request, month):
    try:
        challenge_text = [t for m, t in monthly_challenges.items() if m == month]
        context = {
            'text': challenge_text[0],
            'month': month
        }
        return render(request, 'challenge_text.html', context)
    except:
        raise Http404('This month is not supported')


def list_of_months(request):
    context = {
        'months': Month.objects.all()
    }

    return render(request, 'show_list_of_months.html', context)
