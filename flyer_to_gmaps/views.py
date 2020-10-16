import easyocr
from django.shortcuts import redirect, render

from flyer_to_gmaps.django_request_processor import get_ticket_url_from_uploaded_file
from flyer_to_text_script import get_ticket_url_from_file


def index(request):
    return render(request, "index.html")


def results(request):
    if request.method == "POST":
        try:
            # django_request_processor = DjangoRequestProcessor(request)
            uploaded_file = request.FILES["my_image"]
            print(uploaded_file.name)
            ticket_url = get_ticket_url_from_uploaded_file(uploaded_file)
            # text = django_request_processor.read_text_from_django_file("my_image")
        except Exception:
            return "Can't process poster well enough!"
        return redirect(ticket_url)
