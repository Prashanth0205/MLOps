from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''
    This Function returns the list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [r.replace("\n", "") for r in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
            
    return requirements

setup(
    name = "mlops_project",
    version = "0.0.1",
    author = "Prashanth",
    author_email = "vrprashanth5@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)