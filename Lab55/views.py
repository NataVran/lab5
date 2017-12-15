from django.shortcuts import render
from django.views import View

from testApp.models import TovarModel


def index(request):
    return render (request, 'index.html')

class Orders(View):
    def get(self,request):
        data = {
            'orders': [
                {'title': 'Заказ 1', 'id': 1},
                {'title': 'Заказ 2', 'id': 2},
                {'title': 'Заказ 3', 'id': 3}
            ]
        }
        return render(request, 'orders.html', data)

class OrderOb(View):
    def get(self, request, id):
        data = {
            'orders': {
                'id': id
            }
        }
        return render(request, 'order.html', data)
