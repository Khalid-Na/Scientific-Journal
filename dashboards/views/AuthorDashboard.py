from django.shortcuts import render

def author_dash(request):
        user = request.user
        if user.is_authenticated and user.is_author==True:
                return render(request, "dashboards/index.html")
# Create your views here.
def author(request):
        return render(request, "dashboards/index.html")
def authorArticles(request):
        return render(request, "dashboards/authorArticles.html")
def ArticleReview(request):
        return render(request, "dashboards/ArticleReview.html")

        