from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('syms/', views.syms_index, name='index'),
    path('syms/<int:sym_id>/', views.syms_detail, name='detail'),
    path('syms/create/', views.SymCreate.as_view(), name='syms_create'),
    path('syms/<int:pk>/update/', views.SymUpdate.as_view(), name='syms_update'),
    path('syms/<int:pk>/delete/', views.SymDelete.as_view(), name='syms_delete'),
    path('syms/<int:sym_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]
