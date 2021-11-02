from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('registration', views.registration, name='registration'),
    path('login', views.loginview, name='loginview'),
    path('logout', views.logout_view, name='logout_view'),
    path('create_recipe', views.create_recipe, name='create_recipe'),
    path('create_ingridient', views.create_ingridient, name='create_ingridient'),
]
