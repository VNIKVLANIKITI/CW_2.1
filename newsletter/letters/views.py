from django.shortcuts import render
from django.http import HttpResponse
from letters.models import Customer, Mailing
from letters.forms import MailingForm
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


def health_check(request):
    return HttpResponse("service letters is alive")

# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         print(f'{name} ({email})')
#     return render(request, 'letters/index.html')


def get_customer_list(request):
    customer_list = Customer.objects.all()
    context = {
        'object_list': customer_list,
        'name_list': Customer._meta.verbose_name_plural
    }
    return render(request, 'letters/customer_list.html', context)


def get_mailing_list(request):
    mailing_list = Mailing.objects.all()
    context = {
        'object_list': mailing_list,
        'name_list': Mailing._meta.verbose_name_plural
    }
    return render(request, 'letters/mailing_list.html', context)


def get_letters_list(request):
    mailing_list = Mailing.objects.all()
    context = {
        'object_list': mailing_list,
        'name_list': Mailing._meta.verbose_name_plural
    }
    return render(request, 'letters/letters_list.html', context)


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'letters/mailing_delete.html'
    success_url = reverse_lazy('mailing_list')


def mailing_report(request):
    mailings = Mailing.objects.prefetch_related('customers', 'attemtps').all()
    context = {
        'mailings': mailings,
    }
    return render(request, 'letters/mailing_report.html', context)
