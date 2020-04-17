from django.urls import path
from api.views import *
from api.views.views_cbv import CompanyListAPIView, CompanyDetailAPIView, \
    VacancyListAPIView, VacancyDetailAPIView, VacancyTopTenAPIView, CompanyVacancyListAPIView

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:company_id>', company_detail),
    path('companies/<int:company_id>/vacancies', company_vacancies),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>', vacancy_detail),
    path('vacancies/top_ten', vacancy_top_ten),

    path('login/', obtain_jwt_token),
    # path('companies/', CompanyListAPIView.as_view()),
    # path('companies/<int:company_id>', CompanyDetailAPIView.as_view()),
    # path('companies/<int:company_id>/vacancies', CompanyVacancyListAPIView.as_view()),
    # path('vacancies/', VacancyListAPIView.as_view()),
    # path('vacancies/<int:vacancy_id>', VacancyDetailAPIView.as_view()),
    # path('vacancies/top_ten', VacancyTopTenAPIView.as_view()),
]