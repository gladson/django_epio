#!/usr/bin/env python
# coding: utf-8
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings
from gladson.portal.models import *


class MessageAdmin(admin.ModelAdmin):
    list_display = ['message']

admin.site.register(Message, MessageAdmin)