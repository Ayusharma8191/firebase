"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-10$0@jkjpuo5gynrmquh9^)i%@*w0(*1_ukq5!-k#e&)p73ei@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_sso.sso_service',
    'user_auth',
    'user_fields'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = '/'
SSO_ROOT = 'https://accounts.google.com/o/saml2/idp?idpid=C04ktruyj'
    
# # Specify application token obtained in the SSO server admin panel (REQUIRED)
SSO_TOKEN= """-----BEGIN CERTIFICATE-----
            MIIDdDCCAlygAwIBAgIGAYaswv1wMA0GCSqGSIb3DQEBCwUAMHsxFDASBgNVBAoTC0dvb2dsZSBJ
            bmMuMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MQ8wDQYDVQQDEwZHb29nbGUxGDAWBgNVBAsTD0dv
            b2dsZSBGb3IgV29yazELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWEwHhcNMjMwMzA0
            MTMxNTA0WhcNMjgwMzAyMTMxNTA0WjB7MRQwEgYDVQQKEwtHb29nbGUgSW5jLjEWMBQGA1UEBxMN
            TW91bnRhaW4gVmlldzEPMA0GA1UEAxMGR29vZ2xlMRgwFgYDVQQLEw9Hb29nbGUgRm9yIFdvcmsx
            CzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
            MIIBCgKCAQEA53NTulgeKPbLOKTdO9pZIFbbCBH69wcGtry5vDYNZXtWCbnlS/4jJj0r6hDnabd0
            4Ik0no9DYW12rr+IYU3QuQFYVvAmB2WBkoA3YqYdQrgIe6WT0SkMkdzjKCO5n0mKl1u5joSZ5wm/
            YeAnx6f7XTfO3UkYwXG/dQFZ1WwLL7iVKVW2bMDIyUDWa/5Zg2N0/xa0wHmKJ7axHCA1MDAw33I8
            Yzy5YUWiSwbDaXBLiGI8I2mWhSZzj+PSNvrPulxYBf22TQ2GIOsWJpC5jDJ0wxW4TIbCz6QZVnub
            5k/rIYN0pUIH5AOmP5yAQtuEKh1B5iyePaJijCWu91l11H3NgQIDAQABMA0GCSqGSIb3DQEBCwUA
            A4IBAQAR1YHdkMRb/w/ONTnaeGt6deex5WzwWbwj5ESsMy2gqBpmG4RW47X4KEX/pIinh+owSG+a
            9US3YgBwyVFmg0PUFp98bPsFfjV8Mf+b6Se1HzeUaZ/bDXUgOTdP7jpBCedAU9zov/B9HKcyZTZS
            lDJYSZoJxQDtr2lvOyJkmq485IFa7rCVtF1kL3VIJ12ArVdp6jD8zBA6aCwY3FLanN2QabbAYzLz
            Ph1mVJgwBb5NC0/0eq0r7dtR2kre7BO0x7Hqzl+t/Edx9hAhIrZRpVCWnHNJEbZtt39aL92x1U5t
            g30rhOIn3auXU7wazlD9kaJtqY4DNVA6rKB8ih5+Go5+
            -----END CERTIFICATE-----
            """
 	
# Overriding event acceptor class (OPTIONAL). For more details read
# "Overriding event acceptor in subordinated service" partition
# 'EVENT_ACCEPTOR_CLASS': 'project.my_overrides.MySSOEventAcceptor'


