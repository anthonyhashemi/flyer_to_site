import easyocr
from django.http import HttpResponse
from django.shortcuts import redirect, render

from flyer_to_gmaps.django_request_processor import get_ticket_url_from_uploaded_file
from flyer_to_text_script import get_ticket_url_from_file


def index(request):
    return render(request, "index.html")


def results(request):
    if request.method == "POST":
        try:
            uploaded_file = request.FILES["my_image"]
            print(uploaded_file.name)
            ticket_url = get_ticket_url_from_uploaded_file(uploaded_file)
        except Exception:
            return HttpResponse("Can't process poster well enough!")
        return redirect(ticket_url)
