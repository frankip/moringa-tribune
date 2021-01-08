from django.shortcuts import render
from django.http import HttpResponse

from .models import Article, tags, Editor

# Create your views here.


def welcome(request):
    #logic
    return render(request, 'welcome.html')

def landing_page(request):
    return render(request, 'homepage.html')


def retrieve_articles(request):
    # querry the database
    articles = Article.objects.all()
    
    context = {
        'articles': articles,
        'title': "Moringa tribune blog",
    }

    return render(request, 'articles.html', context)


def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")


        searched_articles = Article.objects.filter(title__icontains=search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def single_article(request, article_id):

    # article = Article.objects.get(id = article_id)
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise http404()


    context = {
        "article": article,
    }
    # import pdb; pdb.set_trace()
    return render(request, 'single-article.html', context)