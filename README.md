# python-3-bootcamp

Tests and assignments exercises for Python 3. This cover the fundamentals and advanced python concepts. Some challenges worth checking out, Tic-tac-toe game.  

## Getting started

The .ipynb extensions can be run using Jupyter Notebook. While the .py extensions using an IDE, in both cases it's recommended to use a virtual env. 

- Clone repository
- Create the virtual directory (`mkdir ~/.virtualenvs`)
- Install Python 3 (`brew install python3`)
- Install virtualenvwrapper (`pip3 install --user virtualenvwrapper`)

In your .bash_profile or .zshrc:

```
alias python=/usr/local/bin/python3

export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
export WORKON_HOME=$HOME/.virtualenvs

# Sourcing virtualenvwrapper
source ~/Library/Python/3.7/bin/virtualenvwrapper.sh
```

Restart your terminal.

### Install into virtualenv
These steps should be familiar if you're familiar with python; if you're not, here's a brief guide to installing:

- Create a virtualenv to hold the project (`python3 -m venv ~/.virtualenvs/python_bootcamp`)
- List virtual environments to verify all OK (`lsvirtualenv`)
- Activate using `workon python_bootcamp`
- Install the project into that virtualenv in development mode: `pip3 install -e .`
- Use `deactivate` to leave the virtual environment.

### Running code
Run jupyter (.ipynb extensions)
```jupyter notebook```

### Pylint checks
Pylint checks for bugs and code quality. It follows the style recommended by PEP 8, the Python style guide. 
How to check your code for pylint issues. 

1) Run `pylint somefile.py` or `pylint -ry somefile.py` (for full report)
2) Fix all the issues reported by pylint
3) Re-run `pylint somefile.py`
4) Aim for a score of 10/10 

## Source

[Resource](https://www.udemy.com/complete-python-bootcamp)
