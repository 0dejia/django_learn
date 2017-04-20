from django.shortcuts import render
from shop.models import Goods
# Create your views here.

def showGoodsList(request):
	goodsList = Goods.objects.all()
	return render(request, 'shop/goodsList.html', {'goods':goodsList})

def createGoods(request):
	goods = Goods(name="Books", price=12.77, desc="This is Dapache Books!")
	goods.save()
	goods = Goods(name="Table", price=13.16, desc="This is Wood Table!")
	goods.save()
	goods = Goods(name="Pen", price=12.77, desc="This is water Pen!")
	goods.save()