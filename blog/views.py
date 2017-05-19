from django.shortcuts import render
from blog.models import article, category, navigate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request, page=1):
	all_article = article.objects.all()
	paginator = Paginator(all_article, 3)


	try:
		contacts = paginator.page(int(page))
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render(request, 'blog/index.html', {'articles': contacts, 'categorys': category.objects.all(), 'nav': navigate.objects.all(), 'page':contacts})