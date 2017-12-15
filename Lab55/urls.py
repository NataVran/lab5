from django.conf.urls import url
from django.contrib import admin
from views import index, OrderOb, Orders

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^order/$', Orders.as_view()),
    url(r'^order/(?P<id>\d+)', OrderOb.as_view())
]
