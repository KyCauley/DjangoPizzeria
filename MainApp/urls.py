from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'MainApp'

urlpatterns = [
    path('',views.index,name='index'),
    path('pizzas',views.pizzas,name='pizzas'),
    path('pizza/<int:pizza_id>/',views.pizza,name='pizza'),
    path('comment/<int:pizza_id>/',views.comment,name='comment'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)