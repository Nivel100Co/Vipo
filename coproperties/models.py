from django.db import models
from user.models import *


class Coproperty(models.Model):
    """Models to set the Coproperty types allowed
    """
    Name = models.CharField(
        max_length = 100,
        verbose_name = 'Name',
        )

    Manager = models.ForeignKey(
        'user.Users',
        null = True,
        blank = True,
        verbose_name = 'User Manager',
        on_delete=models.CASCADE,
        related_name = 'UserManagerCoproperty'

        )


    Address = models.CharField(
        max_length = 80,
        blank = True,
        null = True,
        verbose_name = 'Address',
        )

    Phone = models.CharField(
        max_length = 30,
        blank = True,
        null = True,
        verbose_name = 'Phone',
        )

    City = models.ForeignKey(
        'user.Cities',
        null = True,
        blank = True,
        verbose_name = 'Coproperty City',
        on_delete=models.CASCADE,
        )

    Country = models.ForeignKey(
        'user.Country',
        null = True,
        blank = True,
        verbose_name = 'Coproperty Country',
        on_delete=models.CASCADE,
        )

    Active = models.BooleanField(
        verbose_name = 'Active',
        default=True
        )

    CreateDate = models.DateTimeField(
    	auto_now_add=True,
    	verbose_name = 'Creation Date',
    	)


    UserCreate = models.ForeignKey(
        'user.Users',
        null = True,
        blank = True,
        verbose_name = 'Users Create',
        on_delete=models.CASCADE,
        related_name = 'UserCreateCoproperty'
        )


    Icon = models.ImageField(
        upload_to='icon/CopropertyImage/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        )

    def __str__(self):
        return self.Name


class Property(models.Model):
    """Models to set the Coproperty types allowed
    """

    Code = models.CharField(
        max_length = 80,
        verbose_name = 'Code',
        null = True,
        blank = True,
        )

    Number = models.CharField(
        max_length = 80,
        verbose_name = 'House/Apartment',
        null = True,
        blank = True,
        )

    Letter = models.CharField(
        max_length = 80,
        verbose_name = 'Block',
        null = True,
        blank = True,
        )

    Coproperty = models.ForeignKey(
        'Coproperty',
        null = True,
        blank = True,
        verbose_name = 'Coproperty',
        on_delete=models.CASCADE,
        )

    User = models.ManyToManyField(
    	'user.Users',
    	verbose_name = 'Users',
    	related_name = 'PropertyUsers', 
        symmetrical=False, 
        through="PropertyPhones",
        through_fields=(
            'Property',
            'User'
            )
    	)


    Active = models.BooleanField(
        verbose_name = 'Active',
        default=True
        )

    CreateDate = models.DateTimeField(
    	auto_now_add=True,
    	verbose_name = 'Creation Date',
    	)


    UserCreate = models.ForeignKey(
        'user.Users',
        null = True,
        blank = True,
        verbose_name = 'Users Create',
        on_delete=models.CASCADE,
        related_name = 'UserCreateProperty'
        )


    Icon = models.ImageField(
        upload_to='icon/PropertyImage/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        )

    def __str__(self):
        return self.Code



class PropertyPhones(models.Model):
    """Models to set the Coproperty types allowed
    """


    Property = models.ForeignKey(
        'Property',
        null = True,
        blank = True,
        verbose_name = 'Property',
        on_delete=models.CASCADE,
        )

    User = models.ForeignKey(
        'user.Users',
        null = True,
        blank = True,
        verbose_name = 'Users',
        related_name = 'PropertyPhoneUsers', 
        on_delete=models.CASCADE,
        )

    Principal = models.BooleanField(
        verbose_name = 'Principal',
        default=False
        )


    Phone = models.BigIntegerField(
        verbose_name = 'Phone'
        )

    Active = models.BooleanField(
        verbose_name = 'Active',
        default=True
        )

    CreateDate = models.DateTimeField(
        auto_now_add=True,
        verbose_name = 'Creation Date',
        )


    UserCreate = models.ForeignKey(
        'user.Users',
        null = True,
        blank = True,
        verbose_name = 'Users Create',
        on_delete=models.CASCADE,
        related_name = 'UserCreatePropertyPhone'
        )


    Icon = models.ImageField(
        upload_to='icon/PropertyImage/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        )

    def __str__(self):
        return self.Property.Code





