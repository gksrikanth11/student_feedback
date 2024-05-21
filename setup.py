from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    
    '''
    this funciton will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name='student_feedback',
    version='0.0.1',
    author='Srikanth',
    author_email='srikanth11@gmail.com',
    packages=find_packages(),
    instal_requires=get_requirements('requirements.txt')
)


