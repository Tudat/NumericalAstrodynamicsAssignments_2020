from matplotlib import lines
import matplotlib.pyplot as plt
import numpy as np
import os
import random


class Plot_to_tex:
    """Plots incoming images and/or tables to a latex report with a certain layout."""
    """
    Example of how to include an exported table into your latex report.

    \begin{table}[H]
        \centering
        \caption{Results some computation.}\label{tab:some_computation}
        \begin{tabular}{|c|c|} % remember to update this to show all columns of table
            \hline
            \input{latex/project3/tables/q2.txt}
        \end{tabular}
    \end{table}
    """
    def __init__(self):
        self.script_dir = self.get_script_dir()
        
        
    def plotSingleLine(self,x_path,y_series,x_axis_label,y_axis_label,label,filename,legendPosition,project_nr):
        """Outputs a plot with a single line to a latex report

        :param x_path: x coordinates of a line
        :param y_series: y coordinates of a line
        :param x_axis_label: label of x axis 
        :param y_axis_label: label of y axis 
        :param label: string describing the line (label)
        :param filename: filename of the image that is exported to latex
        :param legendPosition: integer in range 1 to 4 representing the legend position (or string 'best')
        :param project_nr: the number identifying to which latex project this image is exported

        """
        fig=plt.figure();
        ax=fig.add_subplot(111);
        ax.plot(x_path,y_series,c='b',ls='-',label=label,fillstyle='none');
        plt.legend(loc=legendPosition);
        plt.xlabel(x_axis_label);
        plt.ylabel(y_axis_label);
        plt.savefig(os.path.dirname(__file__)+'/../../../latex/project'+str(project_nr)+'/Images/'+filename+'.png');
#         plt.show();


    def plotMultipleLines(self,x,y_series,x_label,y_label,label,filename,legendPosition,project_nr):
        """Outputs a plot with mulltiple lines to a latex report

        :param x: list of x coordinates of the lines of the plot
        :param y_series: y coordinates of the lines of the plot 
        :param x_label: label of x axis 
        :param y_label: label of y axis 
        :param label: list of strings describing the lines (labels)
        :param filename: filename of the image that is exported to latex
        :param legendPosition: integer in range 1 to 4 representing the legend position (or string 'best')
        :param project_nr: the number identifying to which latex project this image is exported

        """
        fig=plt.figure();
        ax=fig.add_subplot(111);

        # generate colours
        cmap = self.get_cmap(len(y_series[:,0]))

        # generate line types
        lineTypes = self.generateLineTypes(y_series)

        for i in range(0,len(y_series)):
            # overwrite linetypes to single type
            lineTypes[i] = "-"
            ax.plot(x,y_series[i,:],ls=lineTypes[i],label=label[i],fillstyle='none',c=cmap(i)); # color

        # configure plot layout
        plt.legend(loc=legendPosition);
        plt.xlabel(x_label);
        plt.ylabel(y_label);
        plt.savefig(os.path.dirname(__file__)+'/../../../latex/project'+str(project_nr)+'/Images/'+filename+'.png');
        
        print(f'plotted lines')

    
    def get_cmap(n, name='hsv'):
        """Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
        RGB color; the keyword argument name must be a standard mpl colormap name.
        Source: https://stackoverflow.com/questions/14720331/how-to-generate-random-colors-in-matplotlib

        :param n: number of lines that need a distinct colour
        :param name:  (Default value = 'hsv') the type of linecolour palet, e.g. rainbow, grayscale etc

        """
        return plt.cm.get_cmap(name, n)


    def generateLineTypes(y_series):
        """Generates returns a list of a vissible line type for each incoming line/y_series

        :param y_series: list with list of y-coordinates representing the lines

        """
        # generate varying linetypes
        typeOfLines = list(lines.lineStyles.keys())

        while(len(y_series)>len(typeOfLines)):
            typeOfLines.append("-.");

        # remove void lines
        for i in range(0, len(y_series)):
            if (typeOfLines[i]=='None'):
                typeOfLines[i]='-'
            if (typeOfLines[i]==''):
                typeOfLines[i]=':'
            if (typeOfLines[i]==' '):
                typeOfLines[i]='--'
        return typeOfLines
        
        
    def put_table_in_tex(self, table_matrix,filename,project_nr):
        """Outputs a table into a latex report

        :param table_matrix: numpy array with the table data
        :param filename: filename of the table that is exported to latex
        :param project_nr: the number identifying to which latex project this table is exported

        """
        cols = np.shape(table_matrix)[1]
        format = "%s"
        for col in range(1,cols):
            format = format+" & %s"
        format = format+""
        plt.savetxt(os.path.dirname(__file__)+"/../../../latex/project"+str(project_nr)+"/tables/"+filename+".txt",table_matrix, delimiter=' & ', fmt=format, newline='  \\\\ \hline \n')

    
    def example_create_a_table(self):
        """Example code that generates the numpy array with 
        table data that can be exported to a latex table. Can 
        be modified to generate your own latex table"""
        project_nr = "1"
        table_name = "example_table_name"
        rows = 2;
        columns = 4;
        table_matrix = np.zeros((rows,columns),dtype=object)
        table_matrix[:,:]="" # replace the standard zeros with emtpy cell
        print(table_matrix)
        for column in range(0,columns):
            for row in range(0,rows):
                table_matrix[row,column]=row+column
        table_matrix[1,0]="example"
        table_matrix[0,1]="grid sizes"

        self.put_table_in_tex(table_matrix,table_name,project_nr)
        
    
    def get_script_dir(self):
        """returns the path of the directory of this script"""
        return os.path.dirname(__file__)


if __name__ == '__main__':
    main = Plot_to_tex()
    main.example_create_a_table()