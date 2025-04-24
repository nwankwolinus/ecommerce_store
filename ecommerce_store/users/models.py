from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom user model to extend the default User
class CustomUser(AbstractUser):
    address = models.TextField(null=True, blank=True)  # User address
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # User phone number

    # Adding related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Custom related name
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Custom related name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )

    def __str__(self):
        return self.username  # Display username in admin panel
