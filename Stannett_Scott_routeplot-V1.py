###Route_Plot v1.0 by Scott Stannett###
###Programme is designed to read text route direction files and show the route plotted on a grid. Upon closing the displayed grid the user will be prompted to input the next file. If the plotted path strays out of the 12 x 12 grid an error will be displayed. The programme stops if teh user inputs "stop".###

import os
import matplotlib.pyplot as plt
import sys

###create a function that will carry out the plotting the route###

def plot_path():
        
###look at the open file, convert into list and remove carriages###
        
        with open(file,"r") as file_object:
            contents= file_object.readlines()

        for i in range(len(contents)):
            contents[i]=contents[i].replace('\n','')
            
###Define starting position and create a list of directions###
            
        startpos = ((int(contents[0])),(int(contents[1])))

        directions = contents[2:]
        
###Define path list and append on the starting position###
        
        path= []
        path.append(startpos)

###adjust starting position by 1 for each direction ###

        for d in directions:
            if d == "N":
                startpos= (startpos[0],startpos[1]+1)
                path.append(startpos)
            elif d == "S":
                startpos= (startpos[0], startpos[1]-1)
                path.append(startpos)
            elif d == "E":
                startpos= (startpos[0]+1, startpos[1])
                path.append(startpos)
            else:
                startpos= (startpos[0]-1, startpos[1])

                path.append(startpos)

            if ((startpos[0] > 12) or (startpos[0] < 0)) or ((startpos[1] > 12) or (startpos[1] < 0)):
                print("Error: The route is outside of the grid, please check input file.")
                break
            
        print("Coordinate List", path)

###plot out path and display###

        xs = [x[0] for x in path]
        ys = [x[1] for x in path]
        plt.plot(xs, ys, linestyle = 'dashed', color = "firebrick", linewidth = 1, marker = "x")
        plt.title ("Plotted Route from Input Directions")
        plt.xlim(0,12)
        plt.ylim(0,12)
        plt.grid(color= "green")
        plt.show() 

###Input file and check it exists in the directory. If it exists the plot_path function begins, if STOP is the input, cease the function###


while True:
        file = input("Please Enter the First Route File i.e. Route001. Type Stop to exit the programme:" ).capitalize()+".txt"
                
        if file == "Stop.txt":
                print("Terminating")
                exit()

        if os.path.isfile(file):
                plot_path()
        else:
                print('File not found. Try again.')
        continue
