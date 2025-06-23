# DJANGO IMPORTS
from django.db import models

# CKEDITOR IMPORTS
from ckeditor.fields import RichTextField

# PRIVACY POLICY MODEL
class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    is_active = True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
# PRIVACY POLICY MODEL
class TermsAndConditions(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    is_active = True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title