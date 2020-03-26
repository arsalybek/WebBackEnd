from django.shortcuts import render
from django.http.response import JsonResponse

from api.models import Product
from api.models import Category


def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': 'product does not found'})

    return JsonResponse(product.to_json())


def category_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': 'category does not found'})

    return JsonResponse(category.to_json())


def products_by_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': 'category does not found'})

    products = category.product_set.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)
