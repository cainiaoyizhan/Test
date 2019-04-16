from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .viewspicture import *

urlpatterns = [
    url(r'^$',index),
    url(r'^register/$',register),
    url(r'^check_username$',check_username),
    url(r'^search$',search),
    url(r'^product$',product),
    url(r'^price$',price_view),
    url(r'^diploma$',diploma_view),
    url(r'^payway$',payway_view),
    url(r'^about$',about_view),
    url(r'^contact$',contact_view),
    url(r'^user$',user_view),
    url(r'^address$',address),
    url(r'^book$',book),
    url(r'^product_d/(?P<id>\d+)/$',product_d),
    url(r'^repwd$',repwd),
    url(r'^shopcar',shopcar),
    url(r'^isDelete/(?P<id>\d+)/',isDelete),
    url(r'^add_product/(?P<id>\d+)/',add_product),
    url(r'^logout/$',logout),
    url(r'^order$',order),
    url(r'^verifycode/$',verifycode),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)