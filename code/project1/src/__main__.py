import os
from .Main import Main
from .Compile_latex import Compile_latex

print(f'Hi, I\'ll be running the main code, and I\'ll let you know when I\'m done.')
project_nr = 1
main = Main()

# compile the latex report
compile_latex =Compile_latex(project_nr ,'main.tex')
exit()

# run the jupyter notebooks for assignment 1 
main.run_jupyter_notebooks()

# convert jupyter notebook for assignment 1 to pdf
main.convert_notebook_to_pdf()

# compile the latex report
compile_latex =Compile_latex(project_nr ,'main.tex')

################################################################
############example code to illustrate latex  image sync###############
################################################################   
# run a genetic algorithm to create some data for a plot.
print("now running a")
res = main.do_run_a()

# plot some graph with a single line, general form is:
# plt_tex.plotSingleLines(plt_tex,x,y,"x-axis label","y-axis label",lineLabels,"filename",legend_position,project_nr)
# main.plt_tex.plotSingleLine(plt_tex,range(0, len(res)),res,"[runs]]","fitness [%]","run 1","4a",4,project_nr)

# run a genetic algorithm to create some data for another plot.
print("now running b")
main.do4b(project_nr)

# run a genetic algorithm to create some data for another plot.
print("now running 4c")
main.do4c(project_nr)

print(f'Done.')