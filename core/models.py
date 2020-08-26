from django.db import models

class Business(models.Model):
    manager_first_name = models.CharField(max_length=50)
    manager_last_name = models.CharField(max_length=50)
    manager_email = models.EmailField(max_length=50)
    # TODO check phone number field for validation
    manager_phone_number = models.CharField(max_length=20)
    business_name = models.CharField(max_length=50)
    business_email = models.EmailField(max_length=50)
    business_country = models.CharField(max_length=50)
    business_city = models.CharField(max_length=50)
    business_address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.business_name}'



class CommunityManager(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    # TODO check phone number field for validation
    phone_number = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name}'
