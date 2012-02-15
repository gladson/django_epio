#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render_to_response

def index(request):
    return render_to_response(
    	"portal/index.html",{
        "message": u"Oi meu bem, não fica com raiva de mim!",
    })