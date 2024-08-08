from django.contrib import admin
from .models import Point

class PointAdmin(admin.ModelAdmin):
    list_display = ('user', 'points', 'last_updated')
    search_fields = ('user__username',)  # جستجو بر اساس نام کاربری
    list_filter = ('last_updated',)
    readonly_fields = ('last_updated',)  # غیرقابل ویرایش بودن فیلد

# ثبت مدل
admin.site.register(Point, PointAdmin)

