class Libro:
    def __init__(self, nombre, capitulos=[], autor="Undefined"):
        self.Nombre = nombre
        self.Capitulos = capitulos
        self.Autor = autor
    
    def __str__(self):
        texto = 'Nombre: ' + self.Nombre
        texto += '\nCapítulos:'
        if self.Capitulos:
            for capitulo in self.Capitulos:
                texto += str(capitulo)
        else:
            texto += 'NO HAY CAPÍTULOS'
        return texto

class Capitulo:
    def __init__(self, nombre, url):
        self.Nombre = nombre
        self.URL = url
    def __str__(self):
        texto = '\nCapítulo {'
        texto += '\n\tNombre: ' + self.Nombre
        texto += '\n\tURL: ' + self.URL + '}'
        return texto

class CapituloHTML:
    def __init__(self, nombre, html):
        self.Nombre = nombre
        self.HTML = html
    def __str__(self):
        texto = '\nCapítulo {'
        texto += '\n\tNombre: ' + self.Nombre
        texto += '\n\HTML: ' + self.HTML + '}'
        return texto
