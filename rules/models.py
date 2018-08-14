from django.db import models
from user.models import *
from coproperty.models import *


class PropertyRules(models.Model):
    """Models to set the Coproperty types allowed
    """

    Name = models.CharField(
        max_length = 80,
        verbose_name = 'Name',
        null = True,
        blank = True,
        )


    Coproperty = models.ForeignKey(
        'coproperty.Coproperty',
        null = True,
        blank = True,
        verbose_name = 'Coproperty',
        on_delete=models.CASCADE,
        )

    PublishDate = models.DateTimeField(
        verbose_name = 'Publish Date',
        )

    Finish = models.DateField(
        verbose_name = 'Finish Date',
        )

    Active = models.BooleanField(
        verbose_name = 'Active',
        default=True
        )

    CreateDate = models.DateTimeField(
    	auto_now_add=True,
    	verbose_name = 'Creation Date',
    	editable = False,
    	)


    UserCreate = models.ForeignKey(
        'user.Users',
        null = True,
        blank = True,
        verbose_name = 'Users Create',
        on_delete=models.CASCADE,
        related_name = 'UserCreateProperty',
        editable = False,
        )


    Image = models.ImageField(
        upload_to='icon/RuleImage/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        )


    FilePath = models.CharField(
        max_length = 512,
        verbose_name = 'File Path',
        null = True,
        blank = True,
        )


    def __str__(self):
        return self.Name
