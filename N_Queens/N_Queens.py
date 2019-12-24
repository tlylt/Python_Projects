#!/usr/bin/python3
# Credit to Barron Stone for Code Clinic: Python 

from time import time
from tkinter import *
from tkinter import ttk, messagebox
from itertools import permutations

class NQueens():
    def __init__(self,master):
        self.n=8 #num of queens
        self.queens=(0 for i in range(self.n)) #one of the solutions showing where queens are
        self.index=0 #index of current solution
        self.solutions=[] #all possible solutions

        #build GUI
        self.master=master
        self.master.title('NQueens')
        self.master.minsize(400, 470)
        self.master.bind('<Configure>', lambda e:self._draw_board())
        
        #add board
        self.board_canvas = Canvas(self.master)
        self.board_canvas.pack()

        #add control panel
        self.controls_frame =ttk.Frame(self.master)
        self.controls_frame.pack(side=TOP, pady=10)

        #make control panel
        ttk.Label(self.controls_frame, text="Number of Queens:").grid(row=0, column=0)
        self.n_var =StringVar()
        self.n_var.set(self.n)
        Spinbox(self.controls_frame, from_=4,to=99,width=2,textvariable=self.n_var).grid(row=0,column=1)
        ttk.Button(self.controls_frame, text= 'Get Next Solution',command=self._solution_callback).grid(row=1,column=0,columnspan=2)
        self.solution_var =StringVar()
        self.time_var=StringVar()
        self.solution_var.set('--')
        self.time_var.set('--')
        ttk.Label(self.controls_frame,text='Solution:').grid(row=0,column=2,sticky=(E))
        ttk.Label(self.controls_frame,textvariable=self.solution_var).grid(row=0,column=3,sticky=(W))
        ttk.Label(self.controls_frame,text='Elapsed Time:').grid(row=1,column=2,sticky=(E))
        ttk.Label(self.controls_frame,textvariable = self.time_var).grid(row=1,column=3,sticky=(W))

        #make and show first solution
        self._solution_callback()

    def _draw_board(self):
        maxboardsize=min(self.master.winfo_width(),self.master.winfo_height()-70)
        cellsize=maxboardsize//self.n
        self.board_canvas.config(height=self.n*cellsize,width=self.n*cellsize)
        self.board_canvas.delete('all')

        for i in range(self.n):
            for j in range(self.n):
                if (i+j+self.n)%2:
                    self.board_canvas.create_rectangle(i*cellsize,j*cellsize,i*cellsize+cellsize,j*cellsize+cellsize,fill='black')
            
            self.board_canvas.create_text(i*cellsize+cellsize//2,self.queens[i]*cellsize+cellsize//2,
            text=u'\u265B',font=('Arial',cellsize//2),fill='orange')

    def _solution_callback(self):
        try:
            input_val = int(self.n_var.get())
        except:
            messagebox.showerror(title='Invalid Input',
            message='Must enter a number for N')
            return
        
        #check if there is a change in input or it is the first run
        if self.n != input_val or self.solutions ==[]:
            if input_val<4:
                messagebox.showerror(title="Invalid Value for N",message="N must be greater than 4.")
            else:
                self.n = input_val #update input
                self.index=0 #reset index
                self.solutions=[] #reset solutions
                start_time=time() #track start time

                #find valid solutions
                columns= range(self.n)
                for perm in permutations(columns):
                    diag1 =set() #check for / diagonal
                    diag2 =set() #check for \ diagonal
                    for i in columns:
                        #add/minus col and row number, if two pieces have the same total, they are
                        #on the same diagonal
                        diag1.add(perm[i]+i)
                        diag2.add(perm[i]-i)
                    if self.n == len(diag1) == len(diag2):
                        self.solutions.append(perm)
                
                elapsed_time = time() - start_time
                self.time_var.set('{0:.3f}s'.format(elapsed_time))
        else:
            #move to next solution
            self.index+=1
        
        #set current solution
        self.queens=self.solutions[self.index % len(self.solutions)]
        #show solution status
        self.solution_var.set('{0}/{1}'.format(self.index % len(self.solutions)+1, len(self.solutions)))
        self._draw_board()

def main():
    root=Tk()
    gui=NQueens(root)
    root.mainloop()

if __name__=="__main__":main()