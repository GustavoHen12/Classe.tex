from django.shortcuts import render
from django_tex.core import compile_template_to_pdf
from django.http import HttpResponse

from texToPdf.generate import generateTex

import logging
logger = logging.getLogger(__name__)

def generate (request):
    size = request.GET['quantity']
    logger.error(request.GET['quantity'])
    
    generateTex(int(size))

    template_name = 'temp.tex'
    context = {'foo': 'Bar'}
    PDF = compile_template_to_pdf(template_name, context)
    response = HttpResponse(PDF,  content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="classeTex.pdf"'

    return response