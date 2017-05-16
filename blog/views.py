from django.shortcuts import render
from blog.models import article, category, navigate
# Create your views here.

def index(request):
	all_article = article.objects.all()
	return render(request, 'blog/index.html', {'articles': all_article, 'categorys': category.objects.all(), 'nav': navigate.objects.all()})