from .Compile_latex import Compile_latex
from .Plot_to_tex import Plot_to_tex as plt_tex
from .Run_jupyter_notebooks import Run_jupyter_notebook

from matplotlib import pyplot as plt
from matplotlib import lines
import matplotlib.pyplot as plt
import numpy as np
import random

# define global variables for genetic algorithm example
string_length = 100
mutation_chance= 1.0/string_length
max_iterations = 1500


class Main:
    """Runs jupiter notebooks, then compiles them to pdf
        Exports those notebook pdfs to the latex of this project 
        nr, then compiles the latex report to pdf.
        
        Als runs a genetic algorithm in conventional .py files
        and exports them to the latex report, to illustrate the 
        functionality of the python and latex integration.
        
        Note that the latex is already compiled before the 
        genetic algorith (GA) is ran, so these results of the GA
        are one version behind the latex pdf report.
    """
    
    def __init__(self):
        self.run_jupyter_notebook = Run_jupyter_notebook()
        pass
        
    
    def run_jupyter_notebooks(self,project_nr,notebook_names):
        """calls a method that runs each jupyter notebook in the list of incoming notebook names

        :param project_nr: the numberr identifying which project is being  ran and compiled
        :param notebook_names: list of strings with the names of the notebooks that need to be ran

        """
        notebook_path = f'code/project{project_nr}/src/'
        
        for notebook_name in notebook_names:
            self.run_jupyter_notebook.run_notebook(f'{notebook_path}{notebook_name}')
    
    
    def convert_notebooks_to_pdf(self,project_nr,notebook_names):
        """calls a method that converts each jupyter notebook in the list of incoming notebook names

        :param project_nr: the numberr identifying which project is being  ran and compiled
        :param notebook_names: list of strings with the names of the notebooks that need to be ran

        """
        notebook_path = f'code/project{project_nr}/src/'
        
        for notebook_name in notebook_names:
            self.run_jupyter_notebook.convert_notebook_to_pdf(f'{notebook_path}{notebook_name}')
    
    
    def compile_latex_report(self,project_nr):
        """compiles latex code to pdf

        :param project_nr: the numberr identifying which project is being  ran and compiled

        """
        compile_latex =Compile_latex(project_nr ,'main.tex')
    
    
    ################################################################
    ############example code to illustrate python-latex  image sync#########
    ##############runs arbitrary genetic algorithm, can be deleted###########
    ################################################################
    def count(self,bits):
        """counts how many bits there are in a chromosome

        :param bits: representing values of dna in chromosome(s)

        """
        count = 0
        for bit in bits:
            if bit:
                count = count + 1
        return count


    def gen_bit_sequence(self):
        """generates a random bit sequence that represents a chromosome of DNA"""
        bits = []
        for _ in range(string_length):
            bits.append(True if random.randint(0, 1) == 1 else False)
        return bits


    def mutate_bit_sequence(self,sequence):
        """Randomly changes a bit sequence that changes the chromosome(s) of DNA
        This is simulating for example radiation effects that generate arbitrary new offspring

        :param sequence: sequence of binary bits that represent a chromosome of DNA

        """
        retval = []
        for bit in sequence :
            do_mutation = random.random() <= mutation_chance
            if(do_mutation):
                retval.append(not bit)
            else:
                retval.append(bit)
        return retval


    #execute a run a
    def do_run_a(self):
        """Performs a run of the genetic algorithm, like simulating evolution
         and returns the fitness of the population.
        """

        seq = self.gen_bit_sequence()
        fitness = self.count(seq)
        results = [fitness]
        for run in range(max_iterations-1):
            new_seq = self.mutate_bit_sequence(seq)
            new_fitness = self.count(new_seq)
            if new_fitness > fitness:
                seq = new_seq
                fitness = new_fitness
            results.append(max(results[-1],fitness))
        return results


    #execute a run c
    def do_run_c(self):
        """Performs a run of the genetic algorithm, like simulating evolution
         and returns the fitness of the population.
        """
        seq = self.gen_bit_sequence()
        fitness = self.count(seq)
        results = [fitness]
        for run in range(max_iterations):
            new_seq = self.mutate_bit_sequence(seq)
            new_fitness = self.count(new_seq)
            seq = new_seq
            fitness = new_fitness
            results.append(max(results[-1], fitness))
        return results


    def do4b(self,project_nr):
        """Performs a run of the genetic algorithm, like simulating evolution
         and exports the optimum fitness of the population per generation 
         as an image to the latex report of the incoming project nr.

        :param project_nr: the numberr identifying which project is being  ran and compiled

        """
        optimum_found = 0

        # generate plot data
        plotResult = np.zeros((10,max_iterations), dtype=int);
        lineLabels = []

        # perform computation
        for run in range(10):
            res = self.do_run_a()
            if res[-1] == string_length:
                optimum_found +=1

            # store computation data for plotting
            lineLabels.append(f'Run {run}')
            plotResult[run,:]=res;

        # plot multiple lines into report (res is an array of dataseries (representing the lines))
        # plt_tex.plotMultipleLines(plt_tex,x,y,"x-axis label","y-axis label",lineLabels,"filename",legend_position,project_nr)
        plt_tex.plotMultipleLines(plt_tex,range(0, len(res)),plotResult,"[runs]]","fitness [%]",lineLabels,"4b",4,project_nr)
        print("total optimum found: {} out of {} runs".format(optimum_found,10))

    def do4c(self,project_nr):
        """Performs a run of the genetic algorithm, like simulating evolution
         and exports the optimum fitness of the population per generation 
         as an image to the latex report of the incoming project nr.

        :param project_nr: the numberr identifying which project is being  ran and compiled

        """
        optimum_found = 0

        # generate plot data
        plotResult = np.zeros((10,max_iterations+1), dtype=int);
        lineLabels = []

        # perform computation
        for run in range(10):
            res = self.do_run_c()
            if res[-1] == string_length:
                optimum_found +=1

            # Store computation results for plot
            lineLabels.append(f'Run {run}')
            plotResult[run,:]=res;

        # plot multiple lines into report (res is an array of dataseries (representing the lines))
        # plt_tex.plotMultipleLines(plt_tex,x,y,"x-axis label","y-axis label",lineLabels,"filename",legend_position,project_nr)
        plt_tex.plotMultipleLines(plt_tex,range(0, len(res)),plotResult,"[runs]]","fitness [%]",lineLabels,"4c",4,project_nr)
        
        print("total optimum found: {} out of {} runs".format(optimum_found, 10))

                
    def addTwo(self,x):
        """adds two to the incoming integer and returns the result of the computation.

        :param x: incoming integer

        """
        return x+2

if __name__ == '__main__':
    # initialize main class
    main = Main()