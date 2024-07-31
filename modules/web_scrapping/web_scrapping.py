from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from modules.web_scrapping.clases import Libro, Capitulo, CapituloHTML

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)


def getNovelData(URL):
    driver.get(URL)
    
    # Base Element
    booksDivElement = driver.find_element(By.CLASS_NAME, 'elementor-tabs-content-wrapper')


    #  Title Elements
    books_datatab = []
    bookTitleElement = booksDivElement.find_elements(By.CLASS_NAME, "elementor-tab-title")

    for bookElem in bookTitleElement:
        bookTitle = bookElem.get_attribute("textContent")
        bookObject = Libro(bookTitle)
        bookDataTab = bookElem.get_attribute("data-tab")
        books_datatab.append((bookObject, bookDataTab))
        

    bookContentElements = booksDivElement.find_elements(By.CLASS_NAME, "elementor-tab-content")

    for bookContentElement in bookContentElements:
        bookChapterElements = bookContentElement.find_element(By.CLASS_NAME, 'lcp_catlist')
        book_data_tab = bookContentElement.get_attribute("data-tab")

        capitulos = []
        link_elems = bookChapterElements.find_elements(By.TAG_NAME, 'a')
        for link_elem in link_elems:
            url = link_elem.get_attribute('href')
            nombre = link_elem.get_attribute("textContent")
            capitulos.append(Capitulo(str(nombre), url))
        
        
        for book_datatab in books_datatab:
            if book_datatab[1] == book_data_tab:
                book_datatab[0].Capitulos = capitulos
    
    finalBooks = []
    for book_datatab in books_datatab:
        finalBooks.append(book_datatab[0])

    return finalBooks

def getChaptersHTML(BOOK):

    BookName = BOOK.Nombre

    HTML_Chapters = []
    for Chapter in BOOK.Capitulos:
        ChName = Chapter.Nombre
        ChURL = Chapter.URL

        driver.get(ChURL)

        # inside_article = driver.find_element(By.CLASS_NAME, 'entry-content')
        # parrafos_elem = inside_article.find_elements(By.TAG_NAME, 'p')
        parrafos_elem = driver.find_elements(By.XPATH, '//div[@class="entry-content"]/p')
        parrafos_html = f"<h3>{ChName}</h3><br>"
        for parrafo in parrafos_elem:
            parrafos_html += parrafo.get_attribute('outerHTML')
        
        capitulo = CapituloHTML(ChName, parrafos_html)
        HTML_Chapters.append(capitulo)

    return Libro(BookName, HTML_Chapters)

# def getChaptersHTML(BOOKS):

#     HTML_BOOKS = []

#     for Book in BOOKS:
#         BookName = Book.Nombre
#         HTML_Chapters = []

#         for Chapter in Book.Capitulos:
#             ChName = Chapter.Nombre
#             ChURL = Chapter.URL

#             driver.get(ChURL)

#             # inside_article = driver.find_element(By.CLASS_NAME, 'entry-content')
#             # parrafos_elem = inside_article.find_elements(By.TAG_NAME, 'p')
#             parrafos_elem = driver.find_elements(By.XPATH, '//div[@class="entry-content"]/p')
#             parrafos_html = f"<h3>{ChName}</h3><br>"
#             for parrafo in parrafos_elem:
#                 parrafos_html += parrafo.get_attribute('outerHTML')
            
#             capitulo = CapituloHTML(ChName, parrafos_html)
#             HTML_Chapters.append(capitulo)


#         HTML_BOOKS.append(Libro(BookName, HTML_Chapters))

#     return HTML_BOOKS
            
