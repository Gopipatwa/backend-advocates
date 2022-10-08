from django.urls import path
from api import views



urlpatterns = [
    path('',views.home.as_view()),
    path('advocates/',views.advocates),
    path('advocates/<int:id>',views.advocates),
    path('companies/',views.companies),
    path('companies/<int:id>',views.companies),
]