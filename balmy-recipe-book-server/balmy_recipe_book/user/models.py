import uuid 
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password


# Create your models here.

class User(models.Model):
    """A model to represent a user."""
    
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name="Public Identifier"
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    profile_picture = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """Override save method to hash the password before saving."""
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username if self.username else str(self.uuid)

    class Meta:
        ordering = ['-date_joined']
        verbose_name = "User"
        verbose_name_plural = "Users"
