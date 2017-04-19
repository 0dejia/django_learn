from django.shortcuts import render
from shop.models import Goods
# Create your views here.

def showGoodsList(request):
	goodsList = Goods.objects.all()
	return render(request, 'shop/goodsList.html', {'goods':goodsList})

def createGoods(request):
	goods = Goods(name="Books", price=12.77, desc="This is Dapache Books!")