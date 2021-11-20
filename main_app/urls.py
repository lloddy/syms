from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('syms/', views.syms_index, name='index'),
    path('syms/<int:sym_id>/', views.syms_detail, name='detail'),
]
