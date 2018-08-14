import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


HOSTS = ['127.0.0.1', '192.168.0.8', '192.168.0.9']

VAR_DEBUG = True

DATA_BASE_DEFAULT = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'acp_salud',
        # 'USER': 'acp_salud_user',
        # 'PASSWORD':'Mario512',
        # 'HOST': 'localhost',
        # 'PORT': '3306',
}