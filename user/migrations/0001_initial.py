# Generated by Django 2.0.7 on 2018-08-09 01:49

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Identification', models.CharField(blank=True, max_length=30, null=True, verbose_name='Identification')),
                ('Phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Phone')),
                ('Address', models.CharField(blank=True, max_length=80, null=True, verbose_name='Address')),
                ('BirthDate', models.DateField(blank=True, null=True, verbose_name='Birth Date ')),
                ('ProfileImage', models.ImageField(blank=True, help_text='300x300', max_length=255, null=True, upload_to='icon/ProfileImage/', verbose_name='Profile Image')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='City Name')),
                ('Description', models.TextField(blank=True, null=True, verbose_name='City Description')),
                ('Icon', models.ImageField(blank=True, help_text='300x300', max_length=255, null=True, upload_to='icon/CityImages/', verbose_name='City Image')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Name')),
                ('Description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('Icon', models.ImageField(blank=True, help_text='300x300', max_length=255, null=True, upload_to='icon/GenderImage/')),
            ],
        ),
        migrations.CreateModel(
            name='IdentificationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Name')),
                ('Description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('Icon', models.ImageField(blank=True, help_text='300x300', max_length=255, null=True, upload_to='icon/IdentificationTypeImage/')),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='City',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Cities', verbose_name='Users City'),
        ),
        migrations.AddField(
            model_name='users',
            name='Gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Gender', verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='users',
            name='IdentificationType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.IdentificationType', verbose_name='Identification Type'),
        ),
        migrations.AddField(
            model_name='users',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
