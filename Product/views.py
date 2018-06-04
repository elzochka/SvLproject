from django.shortcuts import render

# Create your views here.
def single_product(request):
    return render(request, "single-product.html")