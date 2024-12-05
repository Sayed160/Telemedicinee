from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class CustomUser(AbstractUser):
    USER_TYPES = [
        ('staff', 'Staff'),
        ('doctor', 'Doctor'),
        ('patient', 'Patinet'),
    ]
    
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='patient', db_index=True)
    contact_number = PhoneNumberField(null=True, blank=True, unique=True)
    is_approved = models.BooleanField(default=False, db_index=True)
    is_email_verified = models.BooleanField(default=False, db_index=True)
    is_active = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return self.username