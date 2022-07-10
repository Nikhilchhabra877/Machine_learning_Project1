### by using this we can import this from anywhere

from typing import List
from setuptools import setup

PROJECT_NAME = "housing.predictor"
VERSION = "0.0.1"
AUTHOR = "Nikhil"
DESCRIPTION  = "First ML Project"
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    '''
    This function is going to return the list which will contains name of libraries required for this project
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

## Declaring variables for our setup function


setup(

    name = PROJECT_NAME,
    version =  VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = ["housing"],
    install_requires = get_requirements_list()
)


if __name__ == "__main__":
    print(get_requirements_list())