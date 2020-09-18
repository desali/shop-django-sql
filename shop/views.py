import random

from django.db import connection
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render, redirect

from .forms import AdminLoginForm, CategoryNewForm, ProductNewForm, CustomerLoginForm

from .models import Category, Product, Admin, Customer


def admin_login(request):
    if request.method == "POST":
        admin = AdminLoginForm(request.POST)

        if admin.is_valid():
            login = admin.cleaned_data['login']
            password = admin.cleaned_data['password']

            admin_result = Admin.objects.raw('select * from "admin" where "login" = %s and "password" = %s',
                                             [login, password])
            if admin_result:
                return redirect('admin_home')
            else:
                print("incorrect login or password")
    else:
        admin = AdminLoginForm()

    return render(request, 'shop/admin_login.html', {
        'form': admin
    })


def admin_home(request):

    categories = list(Category.objects.raw('select * from "category"'))
    products = list(Product.objects.raw('select * from "product"'))

    if request.method == "POST":
        new_category = CategoryNewForm(request.POST)

        if new_category.is_valid():
            title = new_category.cleaned_data['title']
            description = new_category.cleaned_data['description']

            cursor = connection.cursor()
            cursor.execute('insert into "category" ("id", "title", "description") values (%s, %s, %s)',
                           [random.randint(1, 2312312), title, description])
            connection.commit()

            new_category = CategoryNewForm()
            categories = list(Category.objects.raw('select * from "category"'))
    else:
        new_category = CategoryNewForm()

    return render(request, 'shop/admin_home.html', {
        'categories': categories,
        'products': products,
        'form': new_category,
    })


def home(request):
    data = request.session.get('data')

    categories = list(Category.objects.raw('select * from "category"'))
    products = list(Product.objects.raw('select * from "product"'))

    cursor = connection.cursor()
    cursor.execute('select "product"."name", "product"."price", "cart_content"."count"  from "product" right outer join "cart_content" on "product"."id"="cart_content"."product_id"')
    chosen_products = cursor.fetchall()
    total = 0
    chosen_products = [dict(name=i[0], price=i[1], count=i[2]) for i in chosen_products]

    for i in chosen_products:
        total += int(i["price"]) * int(i["count"])

    print(chosen_products)

    return render(request, 'shop/index.html', {
        'customer': data["customer_email"],
        'chosen_products': chosen_products,
        'products': products,
        'categories': categories,
        'total': total
    })


def customer_login(request):
    if request.method == "POST":
        customer = CustomerLoginForm(request.POST)

        if customer.is_valid():
            email = customer.cleaned_data['email']
            password = customer.cleaned_data['password']

            customer_result = Customer.objects.raw('select * from "customer" where "email" = %s and "password" = %s',
                                                   [email, password])

            if customer_result:
                data = {
                    "customer_email": email,
                    "products": []
                }
                request.session['data'] = data
                return HttpResponseRedirect('../../')
            else:
                print("incorrect email or password")
    else:
        customer = CustomerLoginForm()
    return render(request, 'shop/customer_login.html', {
        'form': customer
    })


def admin_category_view(request, category_id):
    categories = list(Category.objects.raw('select * from "category"'))
    category = Category.objects.raw('select * from "category" where "id" = %s', [category_id])[0]
    products = list(Product.objects.raw('select * from "product" where "category_id" = %s', [category_id]))

    if request.method == "POST":
        new_product = ProductNewForm(request.POST)

        if new_product.is_valid():
            name = new_product.cleaned_data['name']
            count = new_product.cleaned_data['count']
            price = new_product.cleaned_data['price']

            cursor = connection.cursor()
            cursor.execute(
                'insert into "product" ("id", "name", "count", "price", "photo", "category_id") values (%s, %s, %s, %s, %s, %s)',
                [random.randint(10, 1000), name, count, price, 'images/laptop.png', category_id])
            connection.commit()

            new_product = ProductNewForm()
            products = list(Product.objects.raw('select * from "product" where "category_id" = %s', [category_id]))
    else:
        new_product = ProductNewForm()

    return render(request, 'shop/admin_category_view.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'form': new_product,
    })


def admin_product_page(request, product_id):
    categories = list(Category.objects.raw('select * from "category"'))
    product = Product.objects.raw('select * from "product" where "id" = %s', [product_id])[0]

    if request.method == "POST":
        new_product = ProductNewForm(request.POST, instance=product)

        if new_product.is_valid():
            name = new_product.cleaned_data['name']
            count = new_product.cleaned_data['count']
            price = new_product.cleaned_data['price']

            cursor = connection.cursor()
            cursor.execute(
                'update "product" set "name" = %s, "count" = %s, "price" = %s where "id" = %s',
                [name, count, price, product_id])
            connection.commit()

            return redirect('admin_home')
    else:
        new_product = ProductNewForm(instance=product)

    return render(request, 'shop/admin_product_page.html', {
        'form': new_product,
        'categories': categories,
    })


def products_add(request):
    pid = request.POST.get("id")

    cursor = connection.cursor()
    cursor.execute('select "count" from "cart_content" where "product_id" = %s', [pid])
    count = cursor.fetchone()
    if not count:
        cursor.execute(
            'insert into "cart_content" ("id", "count", "product_id", "cart_id") values (%s, %s, %s, %s)',
            [random.randint(10, 1000), 1, pid, 1])

    else:
        cursor.execute(
            'update "cart_content" set "count" = %s where "product_id" = %s and "cart_id" = %s',
            [count[0] + 1, pid, 1])

    connection.commit()

    return HttpResponse("")
