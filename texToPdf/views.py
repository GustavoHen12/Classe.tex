from django.shortcuts import render
from django_tex.core import compile_template_to_pdf
from django.http import HttpResponse

import logging
logger = logging.getLogger(__name__)

def generate (request):
    logger.error(request.GET['quantity'])
    template_name = 'test.tex'
    context = {'foo': 'Bar'}
    PDF = compile_template_to_pdf(template_name, context)
    response = HttpResponse(PDF,  content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="test.pdf"'

    return response