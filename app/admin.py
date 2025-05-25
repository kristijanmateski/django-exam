from django.utils import timezone

from django.contrib import admin
from app.models import Izlozhba, Umetnik, UmetnichkoDelo


# Register your models here.

class IzlozhbaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(date_kraj__gte=timezone.now())
        return qs


class UmetnikAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False


class UmetnichkoDeloAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.umetnik = request.user.umetnik
        super(UmetnichkoDeloAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.umetnik.user == request.user:
            return True


admin.site.register(Umetnik, UmetnikAdmin)
admin.site.register(UmetnichkoDelo, UmetnichkoDeloAdmin)
admin.site.register(Izlozhba, IzlozhbaAdmin)
