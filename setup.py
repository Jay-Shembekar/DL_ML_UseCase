from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    
    """This function returns the list of required packages.

    Args:
        file_path (str): File Path to the requirements.txt file.

    Returns:
        List[str]: Output of the required packages in a list.
    """
    
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

setup(
    name='dl_ml_usecase',
    version='0.0.1',
    packages=find_packages(),
    author='Jay_Shembekar',
    author_email='shembekarjay@gmail.com',
    install_requires=get_requirements('requirements.txt')
)