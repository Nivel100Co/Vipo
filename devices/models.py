from django.db import models

class OperativeSystem(models.Model):
	"""Operative Systems allowed for devices"""
	Name = models.CharField(
		max_length = 50, 
		verbose_name = 'Operative System'
		)

	Icon = models.ImageField(
		upload_to='icon/SystemOperative/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        verbose_name = 'Icon'
		)

	def __str__(self):
		return self.Name


class DeviceType(models.Model):
	"""General clasification for devices"""

	Code = models.PositiveSmallIntegerField(
		verbose_name = 'Code', 
		primary_key = True
		)

	Name = models.CharField(
		max_length = 50, 
		verbose_name = 'Device Type'
		)

	Icon = models.ImageField(
		upload_to='icon/DeviceType/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        verbose_name = 'Icon'
		)

	def __str__(self):
		return self.Name


class Device(models.Model):
    
	UserOwner = models.ForeignKey(
		'user.Users', 
		verbose_name = 'User Owner',  
		null = True, 
		blank = True,
		on_delete=models.CASCADE, 
		related_name = 'UserOwnerDevice'
		)

	DeviceType = models.ForeignKey(
		'DeviceType', 
		verbose_name = 'DeviceType',
		on_delete=models.CASCADE,
		null = True, 
		blank = True,
		)

	OperativeSystem = models.ForeignKey(
		'OperativeSystem', 
		verbose_name = 'OperativeSystem',  
		null = True, 
		blank = True,
		on_delete=models.CASCADE, 
		)

	DeviceId = models.CharField(
		max_length = 100, 
		verbose_name = 'Device Id'
		)

	SoVersion = models.CharField(
		max_length = 30, 
		verbose_name = 'Operative System Version',  
		null = True, 
		blank = True
		)

	DeviceModel = models.CharField(
		max_length = 50, 
		verbose_name = 'Model', 
		null = True, 
		blank = True
		)

	DeviceName = models.CharField(
		max_length = 50, 
		verbose_name = 'Device Name',
		null = True, 
		blank = True)

	DeviceAlias = models.CharField(
		max_length = 50, 
		verbose_name = 'Device Alias',
		null = True, 
		blank = True
		)

	DateCreated = models.DateTimeField(
		auto_now_add=True, 
		verbose_name = 'Date Create', 
		editable = False
		)

	GCMToken = models.CharField(
		max_length = 350, 
		verbose_name = 'Token GCM', 
		null = True, 
		blank = True
		)

	Active = models.BooleanField(
		default = True, 
		verbose_name = 'Active'
		)

	def __str__(self):

		if self.deviceName is not None:
			return self.owner.username + ' - ' + self.deviceType.name + ' - ' + self.operativeSystem.name + ' - ' + self.deviceName
		return self.owner.username + ' - ' + self.deviceType.name + ' - ' + self.operativeSystem.name

