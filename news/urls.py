from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



from .views import welcome, landing_page, retrieve_articles, search_results, single_article
from . import views

urlpatterns = [
    path('', landing_page, name='home'),
    path('welcome', welcome, name='welcome'),
    path('articles', views.retrieve_articles, name='articles'),
    path('search', search_results, name='search_results'),
    path('articles/<int:article_id>', views.single_article, name='single_article' )
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)