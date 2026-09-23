from cancion import cancion
from musica import catalogo

class Biblioteca:
    def __init__(self):
        self.canciones = []
        self.versiones = {}
        # FOR despues del init - tu catalogo diccionario pasa a objeto Cancion
        for item in catalogo:
            nueva = cancion(item['id'], item['titulo'], item['artista'], item['duracion'], "original")
            self.canciones.append(nueva)

    def agregar_version(self, id_nuevo, titulo, artista, duracion, tipo, id_original):
        # nueva con tipo definido
        self.canciones.append(cancion(id_nuevo, titulo, artista, duracion, tipo))
        if id_original not in self.versiones:
            self.versiones[id_original] = []
        self.versiones[id_original].append(id_nuevo)

    def cargar_versiones_ejemplo(self):
        # aca agregas las nuevas con tipo definido
        self.agregar_version(62, "Bohemian Rhapsody Cover", "Artista X", "5:55", "cover", 1)
        self.agregar_version(70, "Bohemian Rhapsody Live", "Artista X", "6:10", "live", 62)

    def versiones_de(self, id_original):
        if id_original not in self.versiones:
            return [] # caso base
        directas = self.versiones[id_original]
        todas = []
        for version in directas:
            todas.append(version)
            derivadas = self.versiones_de(version)
            for v in derivadas:
                todas.append(v)
        return todas

    def ver_versiones(self, id_original):
        ids = self.versiones_de(id_original)
        lista = []
        for vid in ids:
            for c in self.canciones:
                if c.id == vid:
                    lista.append(c)
        return lista

    def listar(self):
        return self.canciones
biblio = Biblioteca()
biblio.cargar_versiones_ejemplo()

print("listar:", [c.titulo for c in biblio.listar()])
print("versiones_de(1):", biblio.versiones_de(1)) # [62, 70]
print("versiones_de(3):", biblio.versiones_de(3)) # []
print("ver_versiones(1):", [c.titulo for c in biblio.ver_versiones(1)])