from django.contrib import admin
from letters.models import Customer, Mailing, Message


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
    search_fields = ('first_name', 'last_name', 'email',)


admin.site.register(Mailing)
admin.site.register(Message)
