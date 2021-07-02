


# PYTHON INSTALLATION NOTES
This project is using virtual environments to manage local development. 
Please consider using the following;
1. venv - [Virtual Environment for modules (Pip module)](https://docs.python.org/3/library/venv.html)
1. pyenv - [Python Installation Management](https://github.com/pyenv/pyenv)

### Create a virtual environment
```
$ pyenv install -l
$ pyenv install 3.9.5

$ python local 3.9.5

$ python --version
Python 3.9.5

$ python -m venv env
```


### Use the Virtual Environemnt
```
python -m venv env
source env/bin/activate
```

### Stop using the Virtual Environment
```
deactivate (STOPS VENV ENV)
```


# Python Usage

## Routes

### /calculate/incometax
#### Parameters
```
year, 
annual income
```

#### Example of route
```
/calculate/incometax?year=2020&annual income=97000
```

## Start
#### Utility Tools
To start the local development server run;
```
./tools/local-start.sh
```

