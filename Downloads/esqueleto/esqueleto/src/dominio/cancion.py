class cancion():
    def __init__(self,id,titulo,autor,duracion,tipo=None):
        self.id=id
        self.titulo=titulo
        self.autor=autor
        self.duracion=duracion
        if not tipo:
         self.tipo = "original"
        else:
         self.tipo = tipo.lower().strip()
        if self.tipo == "":
            self.tipo = "original"
    def es_original(self):
        if self.tipo== 'original':
            return True
        else:
            return False
    def  es_cover(self):
     if self.tipo == 'cover':
         return True
     else:
         return False
    def es_remix(self):
        if self.tipo == 'remix':
            return True
        else: 
            return False
    def es_original(self):
        if self.tipo== 'original':
            return True
        else:
            return False
    def es_live(self):
        if self.tipo== 'live':
            return True
        else: 
            return False      
    def resumen(self):
        return f"{self.id}: {self.nombre} - {self.autor} [{self.tipo}] ({self.duracion})"