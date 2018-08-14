from django.db import models
from user.models import *


class PrivateMessages(models.Model):


    UserReceiver = models.ForeignKey(
        'user.Users',
        null = True,
        blank = True,
        verbose_name = 'User Receiver',
        on_delete=models.CASCADE,
        related_name = 'UserReceiverMessage'

        )


    UserSender = models.ForeignKey(
        'user.Users',
        null = True,
        blank = True,
        verbose_name = 'User Sender',
        on_delete=models.CASCADE,
        related_name = 'UserSenderMessage'

        )


    MessageBody = models.CharField(
        max_length = 80,
        blank = True,
        null = True,
        verbose_name = 'Body',
        )


    CreateDate = models.DateTimeField(
    	auto_now_add=True,
    	verbose_name = 'Creation Date',
		editable = False
    	)

    def __str__(self):
        return srt(self.CreateDate)
