# Python unit test project template with continuous integration (ci).

## usage: do once

0. If you don't have pip: open Anaconda prompt and browse to the directory of this readme and run:
```
cd /home/<your path to the repository folder>/
python get-pip.py
```

1. To use this package, first make a new conda environment and activate (it this automatically installs everything you need)
3.1 For Windows:
```
conda env create --file windows_environment.yml
```
3.2 For Linux:
```
conda env create --file linux_environment.yml
```

## usage: do every time you start Anaconda:

2. Activate the conda environment you created
```
conda activate neumo_project
```

## usage: do every run:

3. Performes run of main code (in `main.py`, called from `__main__.py`)
```
python -m code.project1.src
```

## Testing

4. Testing is as simple as running the following command in the root directory of this repository in Anaconda prompt:
```
python -m pytest
```
from the root directory of this project.


## Note for linux users
The client connection requires sudo rights. I did not install conda as sudo, so ..


<!-- Un-wrapped URL's below (Mostly for Badges) -->
[black_badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[python_badge]: https://img.shields.io/badge/python-3.8-blue.svg
[apache_badge]: https://img.shields.io/badge/license-Apache%202.0-brightgreen.svg
