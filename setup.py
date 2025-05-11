from setuptools import find_packages,setup
#from typing import List

## find_packages-- find packages of all folders
## setup --
## -r (to read and install mutiple file)

def get_requirements()->list[str]:
    
    requirement_list = list[str]= []

    return requirement_list


setup(
    name = 'sensor',
    version = "0.0.1",
    author = "Rishikesh Raj",
    author_email ="rishikeshr335@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements() ,#["pymongo"]
    

    )