from django.contrib import admin
from .models import (
    RaffleChance,
    DiscountCode,
    ConditionalDiscountCode,
    FreeProduct,
    ConditionalCashReward
)

class RewardAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'points_required', 'description')
    search_fields = ('description',)
    list_filter = ('points_required',)

class RaffleChanceAdmin(RewardAdmin):
    list_display = ('name', 'quantity', 'points_required', 'description')
    
class DiscountCodeAdmin(RewardAdmin):
    list_display = ('code', 'product_category', 'discount_percentage', 'valid_from', 'valid_until')
    search_fields = ('code', 'product_category')
    list_filter = ('valid_from', 'valid_until')
    
class ConditionalDiscountCodeAdmin(RewardAdmin):
    list_display = ('code', 'product_category', 'discount_percentage', 'purchase_threshold', 'condition', 'valid_from', 'valid_until')
    search_fields = ('code', 'product_category')
    list_filter = ('condition', 'valid_from', 'valid_until')
    
class FreeProductAdmin(RewardAdmin):
    list_display = ('product_category', 'quantity', 'points_required', 'description')
    
class ConditionalCashRewardAdmin(RewardAdmin):
    list_display = ('discount_value', 'purchase_threshold', 'condition', 'valid_from', 'valid_until')
    list_filter = ('condition', 'valid_from', 'valid_until')

# ثبت مدل‌ها
admin.site.register(RaffleChance, RaffleChanceAdmin)
admin.site.register(DiscountCode, DiscountCodeAdmin)
admin.site.register(ConditionalDiscountCode, ConditionalDiscountCodeAdmin)
admin.site.register(FreeProduct, FreeProductAdmin)
admin.site.register(ConditionalCashReward, ConditionalCashRewardAdmin)

