from django.db import models
from django.conf import settings

class Point(models.Model):
    """مدل برای مدیریت امتیازهای کاربران."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='points',
        help_text="کاربر مربوط به این امتیاز"
    )
    points = models.PositiveIntegerField(
        default=0,
        help_text="تعداد امتیازهای کاربر"
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        help_text="تاریخ آخرین به‌روزرسانی امتیاز"
    )

    def __str__(self):
        return f"{self.user.username} - {self.points} points"

