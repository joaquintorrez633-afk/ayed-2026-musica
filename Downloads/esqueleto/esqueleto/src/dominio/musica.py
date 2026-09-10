catalogo= [
    {'id': 1, 'titulo': 'Bohemian Rhapsody (Live Aid)', 'artista': 'Queen', 'genero': 'Rock', 'anio': 1985, 'duracion': '6:'},
    {'id': 2, 'titulo': 'JiJi','artista': 'Indio Solari', 'genero':'rock', 'anio': 1986, 'duracion': '5:41'},
    {'id': 3, 'titulo': 'Nunca Quise', 'artista': 'Intoxicados', 'genero':'rock', 'anio':2005, 'duracion': '4:21' }
]
def listar_catalogo():
    for item in catalogo:
       print(f' ID: {item['id']} -- Titulo ♪: {item['titulo']} -- Artista: {item['artista']} -- duracion: {item['duracion']}')

listar_catalogo()