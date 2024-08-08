from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from points.models import Point

class Reward(models.Model):
    """مدل پایه برای تمام جوایز. این مدل به عنوان مدل پایه برای ذخیره ویژگی‌های مشترک استفاده می‌شود."""
    points_required = models.PositiveIntegerField(help_text="امتیاز مورد نیاز برای دریافت این جایزه")
    description = models.TextField(blank=True, null=True, help_text="توضیحات اضافی درباره این جایزه")

    class Meta:
        abstract = True  # این مدل به عنوان مدل پایه استفاده می‌شود و خود در پایگاه داده ذخیره نمی‌شود

    def __str__(self):
        return f"{self.__class__.__name__} - {self.id}"

class RewardReference(models.Model):
    """مدل برای مدیریت ارتباط جوایز با امتیازها به صورت عمومی."""
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    points = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='rewards')

    def __str__(self):
        return f"Reward for {self.content_object} with {self.points} points"
        
class RaffleChance(Reward):
    """مدل برای شانس قرعه‌کشی."""
    name = models.CharField(max_length=255, help_text="نام شانس قرعه‌کشی")
    quantity = models.PositiveIntegerField(help_text="تعداد شانس‌های موجود")

    def __str__(self):
        return self.name

class DiscountCode(Reward):
    """مدل برای کد تخفیف محصول خاص."""
    code = models.CharField(max_length=50, unique=True, help_text="کد تخفیف منحصر به فرد")
    product_category = models.CharField(max_length=255, help_text="دسته‌بندی محصول برای کد تخفیف")
    discount_percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="درصد تخفیف بین 1 تا 100"
    )
    valid_from = models.DateTimeField(default=timezone.now, help_text="تاریخ شروع اعتبار کد")
    valid_until = models.DateTimeField(help_text="تاریخ پایان اعتبار کد")

    def is_valid(self):
        """بررسی اعتبار کد تخفیف"""
        now = timezone.now()
        return self.valid_from <= now <= self.valid_until

    def __str__(self):
        return self.code

class ConditionalDiscountCode(Reward):
    """مدل برای کد تخفیف با شرایط سقف خرید."""
    CONDITION_CHOICES = [
        ('greater_than', 'بیشتر از'),
        ('less_than', 'کمتر از'),
    ]
    
    code = models.CharField(max_length=50, unique=True, help_text="کد تخفیف منحصر به فرد")
    product_category = models.CharField(max_length=255, help_text="دسته‌بندی محصول برای کد تخفیف")
    discount_percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="درصد تخفیف بین 1 تا 100"
    )
    purchase_threshold = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="مقدار خریدی که شرط تخفیف بر اساس آن سنجیده می‌شود"
    )
    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        default='greater_than',
        help_text="نوع شرط سقف خرید"
    )
    valid_from = models.DateTimeField(default=timezone.now, help_text="تاریخ شروع اعتبار کد")
    valid_until = models.DateTimeField(help_text="تاریخ پایان اعتبار کد")

    def is_valid(self):
        """بررسی اعتبار کد تخفیف با شرایط"""
        now = timezone.now()
        return self.valid_from <= now <= self.valid_until

    def __str__(self):
        return self.code

class FreeProduct(Reward):
    """مدل برای خرید رایگان محصول."""
    product_name = models.CharField(max_length=255, help_text=" محصول برای خرید رایگان")
    quantity = models.PositiveIntegerField(help_text="تعداد محصولات رایگان")

    def __str__(self):
        return self.product_name

class ConditionalCashReward(Reward):
    """مدل برای تخفیف نقدی با شرایط."""
    CONDITION_CHOICES = [
        ('greater_than', 'بیشتر از'),
        ('less_than', 'کمتر از'),
    ]
    
    discount_value = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="مقدار تخفیف نقدی"
    )
    purchase_threshold = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="مقدار خریدی که شرط تخفیف بر اساس آن سنجیده می‌شود"
    )
    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        default='greater_than',
        help_text="نوع شرط سقف خرید"
    )
    valid_from = models.DateTimeField(default=timezone.now, help_text="تاریخ شروع اعتبار تخفیف")
    valid_until = models.DateTimeField(help_text="تاریخ پایان اعتبار تخفیف")

    def is_valid(self):
        """بررسی اعتبار تخفیف نقدی با شرایط"""
        now = timezone.now()
        return self.valid_from <= now <= self.valid_until

    def __str__(self):
        return f"{self.discount_value} {self.get_condition_display()} {self.purchase_threshold}"

