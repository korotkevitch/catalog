"""agatritual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from agat import views
from agat.views import Catalog, CategoryList, ProductList, IndexView, ServiceView, AboutView, PriceView, ContactView, \
    ThanksView, FeedbackPhoneView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('price', PriceView.as_view(), name='price'),
    path('contact', ContactView.as_view(), name='contact'),
    path('feedback_phone', FeedbackPhoneView.as_view(), name='feedback_phone'),
    path('thanks', ThanksView.as_view(), name = 'thanks'),
    path('service/<service>', ServiceView.as_view(), name='service'),
    path('catalog', Catalog.as_view(), name='catalog'),
    path('catalog/<category>', CategoryList.as_view(), name='category'),
    path('catalog/<category>/<product>', ProductList.as_view(), name='product'),  # Страница товара
    # path('feedback', views.feedback, name="feedback"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
