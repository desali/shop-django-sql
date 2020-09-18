"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from shop import views as app_views

urlpatterns = [
    url(r'^admin/login', app_views.admin_login, name='admin_login'),
    url(r'^admin/home', app_views.admin_home, name='admin_home'),
    url(r'^admin/', admin.site.urls),

    path('', app_views.home, name='home'),
    path('customer/login/', app_views.customer_login, name='customer_login'),
    path('admin/categories/<category_id>/', app_views.admin_category_view, name='admin_category_view'),
    path('admin/products/<product_id>/', app_views.admin_product_page, name='admin_product_page'),

    path('products/add/', app_views.products_add, name='products_add'),
    # url(r'^page/(?P<slug>[-\w]+)/$', app_views.static_page, name='static_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
