from setuptools import setup
from typing import List
#Declaring variable for setup functions
PROJECT_NAME = "housing-predictor"
AUTHOR = "Joti Roy"
REQUIREMENT_FILE_NAME = "requirements.txt"
def get_requirements_list()->List[str] :
    """Description : This function is going to return list of requiremets mention 
    in requirements.txt file
    
    return this function is going to return a list which contain name of lebraries mentioned
    in requirements.txt file"""
    with open(REQUIREMENT_FILE_NAME) as req :
        return req.readlines().remove("-e .")

setup(
    name = PROJECT_NAME,
    version="0.0.2",
    author = AUTHOR,
    description= "This is a first ml project",
    packages=["housing"],
    install_requires = get_requirements_list(),

)


