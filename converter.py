from modules.web_scrapping.web_scrapping import getChaptersHTML, getNovelData
from modules.epub_converter.epub_converter import convertBook


def main(URL):
    BOOKS = getNovelData(URL)

    for libro in BOOKS:
        libroHTML = getChaptersHTML(libro)
        convertBook(libroHTML)


if __name__ == "__main__":
    main('https://novelasligera.com/novela/la-vida-despues-de-la-muerte/')