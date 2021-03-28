from setuptools import setup, find_packages
setup(name='auto-man-system', 
    version='1.0', 
    packages=find_packages(),
    install_requires=[
        'psutil',
        'pandas'
    ])