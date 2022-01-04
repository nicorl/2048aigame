# 2048 AI Game

![2048](./2048.gif)

## Reglas del juego

Grid de 4x4 donde los valores son potencias del valor 2.

Cada vez que movemos, todos los valores que son iguales y están contiguos se suman.

El reto es conseguir un valor de 2048 antes de que nos quedemos sin hueco en el grid.

`2048.py` está basado en [esta](https://github.com/ninja3011/2048-AI/blob/master/2048.py) adaptación. [Original](https://www.youtube.com/watch?v=b4XP2IcI-Bg)

## Entrenamiento 

Enfoque basado en [Monte Carlo](https://es.wikipedia.org/wiki/M%C3%A9todo_de_Montecarlo) donde las posiciones finales son clasificadas como `Win` o `Lose`. En otro caso, alcanzaremos el `límite de movimientos`.

## Destacables de `2048.py`

* `stack()` y `reverse()` son dos funciones que merece la pena entender bien. **stack()** apila y **reverse()** invierte la matriz.


## Para correr el código

1. Genera una ambiente en conda para esto. (yo utilicé python 3.9.9). [Instalar conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)
```conda create --name game2048ai python=3.9.9```

2. Accede al ambiente de conda creado
```conda activate game2048ai```

3. Instala **requirements.txt** dentro del ambiente creado (game2048ai)
``` pip3 install -r requirements.txt```

4. Ejecuta el fichero `agente.py` desde el ambiente creado (game2048ai)