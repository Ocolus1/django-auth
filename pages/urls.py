from django.urls import path

from .views import HomePageView, profile, company_list, company_create, company_detail

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path('profile/', profile, name='profile'),
    path('companies/', company_list, name='company_list'),
    path('companies/new/', company_create, name='company_create'),
    path('companies/<int:company_id>/', company_detail, name='company_detail'),
]
