import os
import tempfile
from typing import List

from django.core.files.storage import default_storage
from django.core.handlers.wsgi import WSGIRequest

from flyer_to_text_script import get_ticket_url_from_file


def get_ticket_url_from_uploaded_file(uploaded_file):
    # name = uploaded_file.name
    name = "tmp_img"
    tmp_file_path = default_storage.path("tmp/" + name)
    with open(tmp_file_path, "wb+") as tmp_file:
        for chunk in uploaded_file.chunks():
            tmp_file.write(chunk)
        tmp_file.seek(0)

        ticket_url = get_ticket_url_from_file(tmp_file_path)
        os.remove(tmp_file_path)
    return ticket_url
