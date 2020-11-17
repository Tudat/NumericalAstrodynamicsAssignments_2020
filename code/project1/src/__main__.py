'''
Runs the main code. 

First it runs the notebooks in this directory
Then it converts those notebooks to pdf
This is followed by compiling the latex  report of this project to pdf.

For illustration purposes, a genetic algorithm is also executed that 
plots some images into the latex report. Since the report is compiled
before the genetic algorithm is ran, the new results are only included
after the second of this main

'''
from .Main import Main
import os

print(f'Hi, I\'ll be running the main code, and I\'ll let you know when I\'m done.')
project_nr = 1
main = Main()

notebook_names = ['AE4868_example_notebook_update20201025.ipynb']

# run the jupyter notebooks for assignment 1 
main.run_jupyter_notebooks(project_nr,notebook_names)

# convert jupyter notebook for assignment 1 to pdf
main.convert_notebooks_to_pdf(project_nr,notebook_names)

# compile the latex report
main.compile_latex_report(project_nr)

################################################################
############example code to illustrate python-latex  image sync#########
##############runs arbitrary genetic algorithm, can be deleted###########
################################################################
# run a genetic algorithm to create some data for a plot.
print("Running method a of Main.py to execute some genetic algorithm")
res = main.do_run_a()

# plot some graph with a single line, general form is:
# plt_tex.plotSingleLines(plt_tex,x,y,"x-axis label","y-axis label",lineLabels,"filename",legend_position,project_nr)
# main.plt_tex.plotSingleLine(plt_tex,range(0, len(res)),res,"[runs]]","fitness [%]","run 1","4a",4,project_nr)

# run a genetic algorithm to create some data for another plot.
print("Running method 4b of Main.py to execute some genetic algorithm")
main.do4b(project_nr)

# run a genetic algorithm to create some data for another plot.
print("Running method 4c of Main.py to execute some genetic algorithm")
main.do4c(project_nr)

print(f'Done with runing code.')