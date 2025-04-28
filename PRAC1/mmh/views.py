from django.shortcuts import render
from .forms import CustomerRegistration
from .models import Product, ProductImage, Category
# Create your views here.
def customer_registration(request):
    if request.method == 'POST':
        fm = CustomerRegistration(request.POST)
        if fm.is_valid():
            cname = fm.cleaned_data['cname']
            cemail = fm.cleaned_data['cemail']
            cpassword = fm.cleaned_data['cpassword']
            print(cname, cemail, cpassword)
            fm = CustomerRegistration()
            return render(request, 'mmh/customerregistration.html', {'form': fm})
        else:
            return render(request, 'mmh/customerregistration.html', {'form': fm})
    else:
        fm = CustomerRegistration()
        return render(request, 'mmh/customerregistration.html', {'form': fm})


def dashboard(request):
    categories = Category.objects.all()

    selected_categories = request.GET.getlist('category')
    print(selected_categories)
    if selected_categories:
        products = Product.objects.filter(category__name__in=selected_categories)
    else:
        # If no category is selected, show all products
        products = Product.objects.all()

    all_products = {
        'categories': categories,
        'products': products,
        'selected_categories': selected_categories
    }
    return render(request, 'mmh/dashboard.html', all_products)