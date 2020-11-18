from nbconvert.preprocessors import ExecutePreprocessor
import os
import nbformat

class Run_jupyter_notebook:
    """runs a list of  jupyter notebooks and converts it to pdf"""

    
    def __init__(self):
        self.script_dir = self.get_script_dir()
        

    def run_jupyter_notebooks(self,project_nr,notebook_names):
        """runs a jupyter notebook in this directory

        :param project_nr: the numberr identifying which project is being  ran and compiled
        :param notebook_names: list of strings with the names of the notebooks that need to be ran

        """
        notebook_path = f'code/project{project_nr}/src/'
        
        for notebook_name in notebook_names:
            self.run_jupyter_notebook.run_notebook(f'{notebook_path}{notebook_name}')
    
    
    def convert_notebooks_to_pdf(self,project_nr,notebook_names):
        """converts a jupyter notebook to pdf

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

    
    def run_notebook(self,notebook_filename):
        """runs a  jupyter notebook that is located in this folder
        
        :param notebook_filename: the name of the notebook that needs to be ran

        """
        # Load your notebook
        with open(notebook_filename) as f:
            nb = nbformat.read(f, as_version=4)

        # Configure
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

        # Execute
        #ep.preprocess(nb, {'metadata': {'path': 'notebooks/'}})
        ep.preprocess(nb, {'metadata': {'path': f'{self.get_script_dir()}'}})

        # Save output notebook
        with open(notebook_filename, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
    
    
    def convert_notebook_to_pdf(self,notebook_filename):
        """Compiles a jupyter notebook that is located in this folder to pdf

        :param notebook_filename: the name of the notebook that needs to be compiled to pdf

        """
        os.system(f'jupyter nbconvert --to pdf {notebook_filename}')
    
    
    def get_script_dir(self):
        """returns the directory of this script regardles of from which level the code is executed"""
        return os.path.dirname(__file__)


if __name__ == '__main__':
    main = Run_jupyter_notebook()