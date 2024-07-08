from datetime import date

from django.template.response import TemplateResponse

# from .models import ???


def index(request):
    return TemplateResponse(
        request,
        "search/index.html",
        {
            "today": date.today(),
        },
    )


