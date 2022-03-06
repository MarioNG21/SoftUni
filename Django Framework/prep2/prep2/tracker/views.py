from django.shortcuts import render, redirect

from prep2.tracker.forms import ProfileCreateForm, ExpenseCreateForm, ExpenseEditForm, ExpenseDeleteForm, \
    EditProfileForm, DeleteProfileForm
from prep2.tracker.models import Profile, Expense


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home(request):
    prof = get_profile()
    if prof is None:
        return home_no_profile(request)
    else:
        expenses = Expense.objects.all()
        money_left = prof.budget - sum(x.price for x in expenses)
    context = {
        'profile': prof,
        'no_profile': False,
        'expenses': expenses,
        'money_left': money_left
    }

    return render(request, 'home-with-profile.html', context)


def home_no_profile(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileCreateForm()

    context = {
        'form': form,
        'no_profile': True
    }
    return render(request, 'home-no-profile.html', context)


def create_page(request):
    if request.method == "POST":
        form = ExpenseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseCreateForm()

    context = {
        'form': form
    }

    return render(request, 'expense-create.html', context)


def edit_page(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExpenseEditForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseEditForm(instance=expense)

    context = {
        'form': form,
        'expense': expense
    }

    return render(request, 'expense-edit.html', context)


def delete_page(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExpenseDeleteForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseDeleteForm(instance=expense)

    context = {
        'form': form,
        'expense': expense
    }
    return render(request, 'expense-delete.html', context)


def profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    total_items = expenses.count()
    budget_left = profile.budget - sum(x.price for x in expenses)
    context = {
        'profile': profile,
        'count': total_items,
        'budget_left': budget_left,

    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    prof = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=prof)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=prof)

    context = {
        'form': form
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    prof = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=prof)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteProfileForm()

    context = {
        'form': form
    }

    return render(request, 'profile-delete.html', context)
