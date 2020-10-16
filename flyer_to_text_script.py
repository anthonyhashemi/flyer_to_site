import easyocr
from googlesearch import search


def get_search_terms(file_path):
    reader = easyocr.Reader(
        ["en"], gpu=False
    )  # need to run only once to load model into memory
    # print(file_path)
    search_terms = reader.readtext(file_path, detail=0)
    print(search_terms)
    return search_terms


def get_ticket_url(search_terms):
    # to search
    # query = "residentadvisor: " + ", '".join(search_terms) + "'"
    query = ", '".join(search_terms) + "'"

    results = search(query, tld="com", num=1, stop=1, pause=2)
    # for j in search(query, tld="com", num=10, stop=10, pause=2):
    #     print(j)
    return next(results)


def get_ticket_url_from_file(file_path):
    return get_ticket_url(get_search_terms(file_path))


# url = get_ticket_url_from_file("images/labyrinth.png")
# print(url)
