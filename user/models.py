from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    """Model that overrides authModel to allow has more information in the same table
    """

    Identification = models.CharField(
        max_length = 30,
        blank = True,
        null = True,
        verbose_name = 'Identification',
        )

    IdentificationType = models.ForeignKey(
        'IdentificationType',
        blank = True,
        null = True,
        verbose_name = 'Identification Type',
        on_delete=models.CASCADE
        )

    Phone = models.CharField(
        max_length = 30,
        blank = True,
        null = True,
        verbose_name = 'Phone',
        )

    City = models.ForeignKey(
        'Cities',
        null = True,
        blank = True,
        verbose_name = 'Users City',
        on_delete=models.CASCADE,
        )

    Country = models.ForeignKey(
        'Country',
        null = True,
        blank = True,
        verbose_name = 'Users Country',
        on_delete=models.CASCADE,
        )

    Address = models.CharField(
        max_length = 80,
        blank = True,
        null = True,
        verbose_name = 'Address',
        )

    BirthDate = models.DateField(
        verbose_name='Birth Date ',
        blank=True,
        null=True,
        )

    Gender = models.ForeignKey(
        'Gender',
        null = True,
        blank = True,
        verbose_name = 'Gender',
        on_delete=models.CASCADE,
        )

    ProfileImage = models.ImageField(
        upload_to='icon/ProfileImage/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        verbose_name = 'Profile Image'
        )

    EPS = models.ForeignKey(
        'EPS',
        blank = True,
        null = True,
        verbose_name = 'EPS',
        on_delete=models.CASCADE
        )


    ARL = models.ForeignKey(
        'ARL',
        blank = True,
        null = True,
        verbose_name = 'ARL',
        on_delete=models.CASCADE
        )


    BloodGroup = models.ForeignKey(
        'BloodGroup',
        blank = True,
        null = True,
        verbose_name = 'Blood Group',
        on_delete=models.CASCADE
        )


    def __str__(self):
        return self.email


class Country(models.Model):
    """Models that contains all cities
    """


    Name = models.CharField(
        max_length = 50,
        verbose_name = 'Country Name',
        )

    Description = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Country Description',
        )
    

    Icon = models.ImageField(
        upload_to='icon/CountryImages/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        verbose_name='Country Image'
        )


    def __str__(self):
        return (self.Name)


class Cities(models.Model):
    """Models that contains all cities
    """


    Name = models.CharField(
        max_length = 50,
        verbose_name = 'City Name',
        )

    Description = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'City Description',
        )
    

    Icon = models.ImageField(
        upload_to='icon/CityImages/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        verbose_name='City Image'
        )


    def __str__(self):
        return (self.Name)


class Gender(models.Model):
    """Models to set the gender types allowed
    """
    Name = models.CharField(
        max_length = 50,
        verbose_name = 'Name',
        )

    Description = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Description',
        )

    Icon = models.ImageField(
        upload_to='icon/GenderImage/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        )

    def __str__(self):
        return self.Name


class IdentificationType(models.Model):
    """Models to set the id types allowed
    """
    Name = models.CharField(
        max_length = 50,
        verbose_name = 'Name',
        )

    Description = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Description',
        )

    Icon = models.ImageField(
        upload_to='icon/IdentificationTypeImage/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        )

    def __str__(self):
        return self.Name



class EPS(models.Model):
    """Models to set the id types allowed
    """
    Name = models.CharField(
        max_length = 50,
        verbose_name = 'Name',
        )

    Description = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Description',
        )

    Icon = models.ImageField(
        upload_to='icon/EPSIcons/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        )

    def __str__(self):
        return self.Name


class ARL(models.Model):
    """Models to set the id types allowed
    """
    Name = models.CharField(
        max_length = 50,
        verbose_name = 'Name',
        )

    Description = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Description',
        )

    Icon = models.ImageField(
        upload_to='icon/ARLIcons/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        )

    def __str__(self):
        return self.Name




class BloodGroup(models.Model):
    """Models to set the id types allowed
    """
    Name = models.CharField(
        max_length = 50,
        verbose_name = 'Name',
        )

    Description = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Description',
        )

    Icon = models.ImageField(
        upload_to='icon/BloodGroupIcons/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        )

    def __str__(self):
        return self.Name


class EmergencyContact(models.Model):
    """Models to set the id types allowed
    """
    User = models.ForeignKey(
        'Users',
        blank = True,
        null = True,
        verbose_name = 'User',
        on_delete=models.CASCADE
        )

    Name = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Description',
        )

    Phone = models.CharField(
        max_length = 30,
        blank = True,
        null = True,
        verbose_name = 'Phone',
        )

    Icon = models.ImageField(
        upload_to='icon/BloodGroupIcons/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        )

    def __str__(self):
        return self.Name



