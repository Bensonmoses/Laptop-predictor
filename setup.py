from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace("/"," ") for req in requirements]
    
    if HYPEN_E_DOT in requiremenst:
        requirements.remove(HYPEN_E_DOT)


setup(
    name = "Ml Project",
    version="0.0.1",
    author="Benson Mosres Palaparthi",
    author_email = "Bensonmoses123@outlook.com",
    packages=find_packages()
    install_requires=get_requiremenst('requiremenst.txt')
)