from django.contrib import admin
from .models import Payment, Order, OrderProduct
# Register your models here.


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'quantity', 'product_price', 'ordered', 'payment')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered']
    readonly_fields = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'ip', 'is_ordered', 'created_at']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]

    # def get_form(self, request, obj=None, **kwargs) :
    #     form = super().get_form(request, obj, **kwargs)
    #     is_superadmin = request.user.is_superadmin
    #     if not is_superadmin:
    #         form.base_fields['full_name'].disabled = True
    #     return form

admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)