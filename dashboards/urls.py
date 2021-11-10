from django.urls import path,include
from .views import AuthorDashboard
app_name = 'dashboards'

urlpatterns = [
        path('author/',AuthorDashboard.author_dash ,name='author'),
        path('author/MyArticle/', AuthorDashboard.authorArticles,name='authorArticles'),
        path('author/ArticleReview/', AuthorDashboard.ArticleReview,name='ArticleReview'),

        # path('reviewer/',include('dashboards.urls')),

]
