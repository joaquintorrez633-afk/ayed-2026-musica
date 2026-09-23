# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## Tema: Musica 

- Elegimos este tema porque nos resultaba mas comodo trabajar con canciones.

## Modelo 

- Item del Catalogo: cada item representa una cancion individual con sus datos (titulo, artista, genero, duracion)

- Elementos inmutables: identificadores de cada cancion (como el tema, artista), una vez que existen no se pueden cambiar.
Decidimos asi para evitar que en un futuro, debido a un accidente (por ejemplo, que una funcion modifique el id de una cancion).

- Elementos mutables: El catalogo en si, en un futuro se puede modificar.
Se decidio asi para que, a medida que avancen las entregas, el catalogo se pueda actualizar sin tener que reahacerlo.

```text
Catálogo (todos los items)
         │
         ▼
Colección principal (ítems activos/gestionados)
      ┌──┴──┐
      ▼     ▼
    Pila   Cola
(historial) (pendiente)
```
 

## 3. Recursión (E2)

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
