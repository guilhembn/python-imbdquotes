from bs4 import BeautifulSoup
from . import utils


def quotes_from_page_id(page_id, max_quotes=utils.DEFAULT_MAX_QUOTES):
    local_page_url = utils.IMBD_URL_QUOTE.format(movie_id=page_id)
    data = utils.html_from_url(local_page_url)
    html_tree = BeautifulSoup(data, 'html.parser')
    return _extract_quotes(html_tree, max_quotes)


def _extract_quotes(tree, max_quotes):
    dialogs = []
    for element in tree.find_all("div"):
        current_dialog = []
        if element.get("class") is not None and "quote" in element.get("class"):
            current_text = None
            for sub in element.descendants:
                if sub.name == "p":
                    current_text = sub.text
                elif sub.name == "span" and sub.get("class") is not None and "character" in sub.get("class"):
                    current_dialog.append({current_text.replace(sub.string, '')[2:].strip(): sub.string})
            dialogs.append(current_dialog.copy())
        if len(dialogs) >= max_quotes:
            break
    return dialogs
