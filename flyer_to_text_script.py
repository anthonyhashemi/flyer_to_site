import pytesseract
import easyocr
from googlesearch import search
from PIL import Image


def get_search_terms(file_path):
    # print(file_path)
    # search_terms = reader.readtext(file_path, detail=0)
    # results = pytesseract.image_to_data(Image.open(file_path))
    results = pytesseract.image_to_data(Image.open(file_path), output_type="data.frame")
    print(results)
    print(results["conf"])
    search_terms = results[results["conf"] > 60]
    print(search_terms)
    search_terms = search_terms["text"]
    print(search_terms)
    search_terms = search_terms.dropna()
    print(search_terms)
    return search_terms


def get_ticket_url(search_terms):
    # to search
    # query = "residentadvisor: " + ", '".join(search_terms) + "'"
    query = "'" + ", '".join(search_terms) + "'"
    print(query)

    results = search(query, tld="com", num=1, stop=1, pause=2)
    # for j in search(query, tld="com", num=10, stop=10, pause=2):
    #     print(j)
    return next(results)


def get_ticket_url_from_file(file_path):
    return get_ticket_url(get_search_terms(file_path))


# url = get_ticket_url_from_file("images/labyrinth.png")
# print(url)
