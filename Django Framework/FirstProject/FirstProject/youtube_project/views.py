from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from FirstProject.youtube_project.forms import ArticleForm
from FirstProject.youtube_project.models import Article


def search_view(request):
    query = request.GET.get('q')
    qs = Article.objects.all()
    if query is not None:
        # qs = Article.objects.filter(title__icontains=query)
        qs = Article.objects.search(query)
    context = {
        'object_list': qs
    }
    return render(request, 'search.html', context)


@login_required
def article_create_view(request):
    context = {
    }

    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            article_obj = form.save()
            context['obj'] = article_obj
            context['is_created'] = True
            return redirect('index')
    else:
        form = ArticleForm()

    context['form'] = form
    return render(request, 'create.html', context)


def article_details_view(request, slug):
    context = {

    }
    article = Article.objects.get(slug=slug)
    if article is None:
        return Http404('This slug does not exits')
    else:
        context['obj'] = article

    return render(request, 'article_details.html', context)
