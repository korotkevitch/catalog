from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views import View
from .models import Catalog, Category, Product, Service, About, Price, Contact, FeedbackPhone
from django.core.mail import BadHeaderError
from .forms import UserForm, UserForm2
from django.views.generic.edit import FormView
from django.core.mail import send_mail


class IndexView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'category_list'

# выносим сюда контекст всех вьюшек, получаемый из БД, чтобы не определять его в каждой отдельно, за исключением
# тех случаев, когда он получается динамически из УРЛа

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category_list'] = Category.objects.all()
        context['service_list'] = Service.objects.all()
        context['about_details'] = About.objects.all()
        context['price_details_1'] = Price.objects.all()[0:3]
        context['price_details_2'] = Price.objects.all()[3:6]
        context['about_details'] = About.objects.all()
        return context


# наследуясь во всех последующих классах от IndexView, мы не только наследуемся от ListView (от которого наследуется
# IndexView) но и имеем доступ к общему для всех страниц контесту, чтобы не прописывать его для каждой страницы, что
# надо для пунктов меню


class ServiceView(IndexView):
    model = Service
    template_name = 'service.html'  # страница с описанием каждой услуги
    context_object_name = 'service_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['current_service'] = get_object_or_404(Service, slug=self.kwargs['service'])
        return context


class PriceView(IndexView):
    model = Price
    template_name = 'price.html'  # страница с описанием каждой услуги
    context_object_name = 'price_details'


class AboutView(IndexView):
    model = About
    template_name = 'about.html'
    context_object_name = 'about_details'


class ContactView(FormView, IndexView):
    model = Contact
    template_name = 'contact.html'
    context_object_name = 'contact_details'
    form_class = UserForm
    success_url = '/thanks'

    def form_valid(self, myform):
        myform.send_mail()
        myform.save()  # сохранение в БД
        return super().form_valid(myform)


class FeedbackPhoneView(FormView):
    model = FeedbackPhone
    form_class = UserForm2
    success_url = '/thanks'

    def form_valid(self, myform):
        myform.send_mail()
        myform.save()  # сохранение в БД
        return super().form_valid(myform)


class ThanksView(IndexView):
    template_name = 'thanks.html'


class Catalog(IndexView):
    model = Catalog
    template_name = 'catalog.html'
    context_object_name = 'category'


class CategoryList(IndexView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'products_of_category'


    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        context = super().get_context_data()
        context['title'] = self.category.cat_name
        context['description'] = self.category.description
        return context


class ProductList(IndexView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'current_product'

    def get_queryset(self):
        return get_object_or_404(Product, slug=self.kwargs['product'])

    def get_context_data(self, **kwargs):
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        context = super().get_context_data()
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['category'])
        context['other_category_products'] = Product.objects.filter(category=self.category).exclude(slug=self.kwargs['product']).order_by('?')[:4]
        return context


####### Данные из формы отправляются на емейл и в БД (админку) ########

# def feedback(request):
#     name = request.POST.get('name', '')
#     phone = request.POST.get('phone', '')
#     message = request.POST.get('message', '')
#     if name and phone and message:
#         try:
#             send_mail('Сообщение с сайта iko-studio.com',
#                       str('Имя:' + ' ' + name + '\n' + 'Телефон:' + ' ' + phone + '\n' + '\n' + 'Сообщение:' + ' ' + message),
#                       'no-reply@iko-studio.com',
#                       ['info@iko-studio.com'])
#
#             f = Feedback(name=name, phone=phone, message=message)  # Данные сохраняются в БД (админке)
#             f.save()
#
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return render(request, 'thanks.html')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return render(request, 'thanks.html')
#
#
# def feedback_phone(request):
#     phone = request.POST.get('phone', '')
#     if phone:
#         try:
#             send_mail('Сообщение с сайта iko-studio.com',
#                       str('Прошу позвонить:' + ' ' + phone),
#                       'no-reply@iko-studio.com',
#                       ['info@iko-studio.com'])
#
#             f = Feedback(phone=phone)  # Данные сохраняются в БД (админке)
#             f.save()
#
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return render(request, 'thanks.html')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return render(request, 'thanks.html')


