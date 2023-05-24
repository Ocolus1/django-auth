from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

def validate_company_create(name, url, logo, category, stage, address, city, state, zip, country, phone):
    if not all([name, url, logo, category, stage, address, city, state, zip, country, phone]):
        raise ValidationError("All fields are required.")
