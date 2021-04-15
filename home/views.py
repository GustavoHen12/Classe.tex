from django.shortcuts import render
from django_tex.shortcuts import render_to_pdf

def home(request):
     # template_name = 'test.tex'
     # context = {'foo': 'Ola mundo'}
     # return render_to_pdf(request, template_name, context, filename='test.pdf')
     return render(request, 'index.html', {'quantity':5})
