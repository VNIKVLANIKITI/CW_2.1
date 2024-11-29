from django.contrib import admin
from django.urls import path
from letters.views import health_check
from .views import health_check as health_general
from letters.views import get_customer_list as get_customer_list
from letters.views import get_mailing_list as get_mailing_list
from letters.views import MailingCreateView, MailingDeleteView, mailing_report
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("letters/alive", health_check),
    path("letters/all", health_check),
    path("general/home", health_general),
    path("", get_customer_list, name='customer_list'),
    path("mailing/list", get_mailing_list, name='mailing_list'),
    path("mailing/create", MailingCreateView.as_view(), name='create_mailing'),
    path('mailing/delete/<int:pk>', MailingDeleteView.as_view(),
         name='mailing_delete'),
    path('mailing/report/', mailing_report, name='mailing_report'),
    path('users/', include('users.urls', namespace='users')),
]
