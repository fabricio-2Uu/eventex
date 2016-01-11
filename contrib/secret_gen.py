#!/usr/bin/env python
"""
Django SECRET_KET generator.
"""
from django.utils.crypto import get_random_string

chars = 'abdefghijklmnopqrstuvwxzy0123456789!@#$%^&*(-_=+)'
print(get_random_string(50, chars))