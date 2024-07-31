from ebooklib import epub
from modules.web_scrapping.clases import CapituloHTML, Libro

def convertBook(libro):


    book = epub.EpubBook()

    # book.set_identifier("id123456")
    book.set_title(libro.Nombre)
    book.set_language("es")

    book.add_author(libro.Autor)

    items = []
    for i, capitulo in enumerate(libro.Capitulos):
        chapter = epub.EpubHtml(title=capitulo.Nombre, file_name=f"chap_{i+1}.xhtml", lang="es")
        chapter.content = capitulo.HTML
        book.add_item(chapter)
        items.append(chapter)

    book.toc = [epub.Link(f'chap_{i+1}.xhtml', cap.Nombre, f'chap_{i+1}') for i, cap in enumerate(libro.Capitulos)]

    # add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # define CSS style
    style = "BODY {color: white;}"
    nav_css = epub.EpubItem(
        uid="style_nav",
        file_name="style/nav.css",
        media_type="text/css",
        content=style,
    )

    # add CSS file
    book.add_item(nav_css)

    # basic spine
    book.spine = ["nav"] + items

    # write to the file
    epub.write_epub(f"{libro.Nombre} - {libro.Autor}.epub", book, {})