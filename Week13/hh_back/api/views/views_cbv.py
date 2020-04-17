from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Company, Vacancy
from api.serializers import CompanySerializer2, VacancySerializer2


class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer2(companies, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CompanyDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, category_id):
        company = self.get_object(category_id)
        serializer = CompanySerializer2(company)
        return Response(serializer.data)

    def put(self, request, category_id):
        company = self.get_object(category_id)
        serializer = CompanySerializer2(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, category_id):
        company = self.get_object(category_id)
        company.delete()

        return Response({'deleted': True})


class VacancyListAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer2(vacancies, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VacancyDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, company_id):
        vacancy = self.get_object(company_id)
        serializer = VacancySerializer2(vacancy)
        return Response(serializer.data)

    def put(self, request, company_id):
        vacancy = self.get_object(company_id)
        serializer = VacancySerializer2(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, company_id):
        vacancy = self.get_object(company_id)
        vacancy.delete()

        return Response({'deleted': True})

class VacancyTopTenAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.order_by('-salary')
        serializer = VacancySerializer2(vacancies, many=True)
        return Response(serializer.data[:10])

class CompanyVacancyListAPIView(APIView):
    def get_object(self, id):
        try:
            return Company.objects.get(id=id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, company_id):
        vacancies = self.get_object(company_id).vacancy_set.all()
        serializer = VacancySerializer2(vacancies, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = VacancySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
