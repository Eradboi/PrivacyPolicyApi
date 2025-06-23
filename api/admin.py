# DJANGO IMPORTS
from django.contrib import admin

# MODEL IMPORTS
from .models import PrivacyPolicy, TermsAndConditions

# REGISTER THE MODELS INTO THE ADMIN
admin.site.register(PrivacyPolicy)
admin.site.register(TermsAndConditions)
