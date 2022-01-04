# -*- coding: utf-8 -*-

#Importamos librerías.
#Tkinter contiene clases que permite mostrar display, posición y control de widgets.
import tkinter as tk 
import random
import colors as c


class Game(tk.Frame): 
    def __init__(self):
        tk.Frame.__init__(self)
        #Position a widget in the parent widget in a grid
        #grid(​padx, pady, row, sticky, column)
        self.grid()
        self.master.title('2048')
        self.main_grid = tk.Frame(
            self,
            bg=c.GRID_COLOR,
            bd=3,
            width=400, 
            height=400
            )
        self.main_grid.grid(pady=((80,0)))
        self.make_GUI()
        self.start_game()

        self.master.bind('<Left>',self.left)
        self.master.bind('<Right>',self.right)
        self.master.bind('<Up>',self.up)
        self.master.bind('<Down>',self.down)

        self.mainloop()

    def make_GUI(self):
        #Genera el grid
        self.cells=[]
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame=tk.Frame(
                    self.main_grid,
                    bg=c.EMPTY_CELL_COLOR,
                    width=100,
                    height=100
                    )
                cell_frame.grid(row=i,column=j,padx=5, pady=5)
                cell_number=tk.Label(self.main_grid,bg=c.EMPTY_CELL_COLOR)
                cell_number.grid(row=i, column=j)
                cell_data ={'frame': cell_frame, 'number': cell_number}
                #Sobreescribe para forzar la validación
                row.append(cell_data)
            self.cells.append(row)

        #Puntuación
        score_frame = tk.Frame(self)
        score_frame.place(relx=0.5,y=40,anchor='center')
        #Etiqueta para mostrar texto y bitmaps
        tk.Label(
            score_frame,
            text='Puntuación',
            font=c.SCORE_LABEL_FONT).grid(row=0)
        self.score_label=tk.Label(score_frame,text='0', font=c.SCORE_FONT)
        self.score_label.grid(row=1)

    def start_game(self):
        # Crear ma triz de 0s
        self.matrix=[[0] * 4 for _ in range(4)]
        # Rellenar dos celda aleatorias con dos 2's.
        # randint(): Devuelve valor en rango [a, b], incluyendo ambos (a y b).
        
        # Generamos el primer 2.
        row = random.randint(0,3)
        col = random.randint(0,3)
        self.matrix[row][col] = 2
        self.cells[row][col]['frame'].configure(bg=c.CELL_COLORS[2])
        self.cells[row][col]['number'].configure(
            bg=c.CELL_COLORS[2],
            fg=c.CELL_NUMBER_COLORS[2],
            font=c.CELL_NUMBER_FONTS[2],
            text='2')

        # Generamos el segundo 2.
        while(self.matrix[row][col] != 0):
            row = random.randint(0,3)
            col = random.randint(0,3)

        self.matrix[row][col] = 2
        self.cells[row][col]['frame'].configure(bg=c.CELL_COLORS[2])
        self.cells[row][col]['number'].configure(
            bg=c.CELL_COLORS[2],
            fg=c.CELL_NUMBER_COLORS[2],
            font=c.CELL_NUMBER_FONTS[2],
            text= '2')

        self.score=0


    # Función para mover las cajas 
    # Esta función se ejecuta cuando se pulsa una tecla    
    def stack(self):
        # Generamos una matriz vacía
        new_matrix = [[0] * 4 for _ in range(4)]
        # iteramos a lo largo y ancho
        for i in range(4):
            fill_position = 0
            for j in range(4):
                # si el valor es distinto a 0
                if(self.matrix[i][j] != 0):
                    # reescribimos el valor
                    new_matrix[i][fill_position]=self.matrix[i][j]
                    # y aumentamos la variable fill_position 
                    fill_position+=1
        self.matrix=new_matrix

    # Función para combinar valores si son iguales
    # Esta función se combina con la anterior y se ejecuta cuando se pulsa una tecla
    def combine(self):
        for i in range(4):
            # iteramos en rango(3) para comparar j contra (j+1) y que no pete
            for j in range(3):
                if(self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j+1]):
                    self.matrix[i][j] *= 2
                    self.matrix[i][j+1] = 0
                    self.score += self.matrix[i][j]

    # Función para dar la vuelta a la matriz
    def reverse(self):
        new_matrix= []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3-j])
        self.matrix=new_matrix

    # Funciónp ara trasponer sobre la diagonal
    def transpose(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix=new_matrix

    # Función para generar un nuevo número 2 (o un 4)
    def add_new_tile(self):
        row=random.randint(0,3)
        col=random.randint(0,3)
        while(self.matrix[row][col] != 0):
            row = random.randint(0,3)
            col = random.randint(0,3)
        self.matrix[row][col]= random.choice([2,4])

        #Actualizar el GUI

    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if( cell_value ==0):
                    self.cells[i][j]['frame'].configure(bg=c.EMPTY_CELL_COLOR)
                    self.cells[i][j]['number'].configure(
                        bg=c.EMPTY_CELL_COLOR,
                        text='')
                else:
                    self.cells[i][j]['frame'].configure(
                        bg=c.CELL_COLORS[cell_value])
                    self.cells[i][j]['number'].configure(
                        bg=c.CELL_COLORS[cell_value],
                        fg=c.CELL_NUMBER_COLORS[cell_value],
                        font=c.CELL_NUMBER_FONTS[cell_value],
                        text=str(cell_value)
                        )
        self.score_label.configure(text=self.score)
        self.update_idletasks()


    def left(self,event):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack() 
        self.reverse()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

        #Dos funciones para comprobar si hay movimientos posibles

    def horizontal_move_exists(self):
        for i in range(4):
            for j in range(3):
                if(self.matrix[i][j] == self.matrix[i][j+1]):
                    return True
        return False

    def vertical_move_exists(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i + 1][j]:
                    return True
        return False

    # Funcion para finalizar el juego
    def game_over(self):
        # Si alcanzas la maxima puntuación
        if any(2048 in row for row in self.matrix):
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5,rely=0.5,anchor='center')
            tk.Label(
                game_over_frame,
                text='You win!',
                bg=c.WINNER_BG,
                fg=c.GAME_OVER_FONT_COLOR,
                font=c.GAME_OVER_FONT).pack()
        # Si no hay mas capacidad de moverse
        elif not any(0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5,anchor='center')
            tk.Label(
                game_over_frame,
                text='Game Over!',
                bg=c.LOSER_BG,
                fg=c.GAME_OVER_FONT_COLOR,
                font= c.GAME_OVER_FONT)

def main():
    Game()

if __name__=='__main__':
    main()
