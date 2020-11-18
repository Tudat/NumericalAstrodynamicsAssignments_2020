# Student course template Numerical Astrodynamics[![Build Status](https://travis-ci.org/a-t-0/NumericalAstrodynamicsAssignments_2020.svg?branch=master)](https://travis-ci.org/a-t-0/NumericalAstrodynamicsAssignments_2020)

Hi, w.r.t. the original repository this repository is supplemented with:

0. Python code and latex report integration. The following is done with a single command: 
  - Plots are exported directly into your latex report.
  - Your python code is automatically included in the appendices of your report.
  - The example jupyter notebook is automatically executed.
  - The example jupyter notebook is automatically converted to pdf
  - The pdf of the example jupyter notebook is automatically integrated in the latex report.
  - The latex report is automatically compiled into a pdf.
1. You can easily sync with overleaf, e.g. if you do a last minute run, you just push and pull into overleaf, instead of manually uploading pictures.
2. Example unit tests are written that test both the python code, as well as the code inside the Jupyter notebooks.
3. All unit tests can be ran with a single command.
4. The continuous integration with Travis-CI runs all the unit tests in this repository automatically for every push towards this repository ('s master branch). If all tests are passed, the above badge is green and says "passed".

**Room for improvement**

5. The code (that I wrote) could be documented more clearly, with proper comment formatting.
6. The code that (executes and) converts the jupyter notebooks to pdf could loop through all notebooks in the respective `/src/`folder automatically in a `try` `catch` block to automatically skip new notebooks that do not yet compile. This would prevent the user from having to specify which notebooks should be compiled.

## Usage: do once

0. If you don't have pip: open Anaconda prompt and browse to the directory of this readme:
```
cd /home/<your path to the repository folder>/
```

1. To use this package, first make a new conda environment (it this automatically installs everything you need).
```
conda env create --file tudat-space_environment.yml
```

## Usage: do every time you start Anaconda:

3. Activate the conda environment you created:
```
conda activate tudat-space
```

## Usage: do every run:

3. Performe a run for assignment 1 (named project1) of main code (in `main.py`, called from `__main__.py`)
```
python -m code.project1.src
```

## Testing

4. Testing is as simple as running the following command in the root directory of this repository in Anaconda prompt:
```
python -m pytest
```
from the root directory of this project.

## Documentation
The docstring documentation (template) was generated using `pyment`. The HTML documentation of the code was 
generated using `pdoc`.

<!-- Un-wrapped URL's below (Mostly for Badges) -->
[black_badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[python_badge]: https://img.shields.io/badge/python-3.8-blue.svg
