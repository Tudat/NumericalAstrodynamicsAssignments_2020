# Upgraded Course template Numerical Astrodynamics[![Build Status](https://travis-ci.org/a-t-0/NumericalAstrodynamicsAssignments_2020.svg?branch=master)](https://travis-ci.org/a-t-0/NumericalAstrodynamicsAssignments_2020)

Hi, w.r.t. the original repository this repository is supplemented with:

0. Python code and latex report integration. 
  - Plots are exported directly into your latex report.
  - Your python code is automatically included in the appendices of your report.
1. You can easily sync with overleaf, e.g. if you do a last minute run, you just push and pull into overleaf, instead of manually uploading pictures.
2. Unit tests are written. (entire repository code can be tested with a single line)
3. Continuous integration (CI) testing is set up with Travis-CI.
4. TODO: auto compile the latex report when you run the code.
5. TODO: auto export jupyter notebook to pdf to include into latex report.

## usage: do once

0. If you don't have pip: open Anaconda prompt and browse to the directory of this readme:
```
cd /home/<your path to the repository folder>/
```

1. To use this package, first make a new conda environment and activate (it this automatically installs everything you need)
1.1 For Windows:
```
conda env create --file windows_environment.yml
```
1.2 For Linux:
```
conda env create --file linux_environment.yml
```
2. Instal jupyter-lab with command:
```
jupyter-lab
```

## usage: do every time you start Anaconda:

3. Activate the conda environment you created:
```
conda activate num_astro
```
4. Open jupyter lab
```
jupyter-lab
```

## usage: do every run:

3. Performe a run for assignment 1 (named project1) of main code (in `main.py`, called from `__main__.py`)
```
python -m code.project 1.src
```

## Testing

4. Testing is as simple as running the following command in the root directory of this repository in Anaconda prompt:
```
python -m pytest
```
from the root directory of this project.

<!-- Un-wrapped URL's below (Mostly for Badges) -->
[black_badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[python_badge]: https://img.shields.io/badge/python-3.8-blue.svg
[apache_badge]: https://img.shields.io/badge/license-Apache%202.0-brightgreen.svg
