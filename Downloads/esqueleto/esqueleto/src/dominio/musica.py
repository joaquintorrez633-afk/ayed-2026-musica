catalogo= [
    {'id': 1, 'titulo': 'Bohemian Rhapsody (Live Aid)', 'artista': 'Queen', 'genero': 'Rock', 'anio': 1985, 'duracion_min': 6},
    {'id': 2, 'titulo': 'JiJi','artista': 'Indio Solari', 'genero':'rock', 'anio': 1986, 'duracion_min': '5:41'},
    {'id': 3, 'titulo': 'Nunca Quise', 'artista': 'Intoxicados', 'genero':'rock', 'anio':2005, 'duracion_min': '4:21' }
]
def listar_catalogo():
    for item in catalogo:
        print(f'{item['id']:>3}   {item ['titulo']}  {item['artista']}' )
        