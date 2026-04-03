'''
The setup.py file is an essential part of packaging and 
distributing python projects. It is used by the setuptools
(or distutils in older python versions) to define the configuration
of your project, such as it's metadata, dependencies and more    
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This functions returns list of requirements
    '''
    requirement_lst:List[str] = []
    try:
        with open(file_path,'r') as file:
            #Read lines from the file
            lines=file.readlines()
            #Process each line
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst

setup(
    name="Network Security",
    version="0.0.1",
    author="Anjali",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)