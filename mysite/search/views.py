from django.template.response import TemplateResponse

from datetime import date

def index(request):
    return TemplateResponse(request, 'search/index.html', {
        'today': date.today(), 
    })



