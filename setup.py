from setuptools import setup, find_packages

setup(
    name='config_reader',
    version='0.1',
    packages=find_packages(),
    description='A module to read various configuration files and handle them as dictionaries.',
    long_description='This module can read .yaml, .cfg, and .conf files, convert them into flat dictionaries, and support writing to .env and .json files or setting environment variables.',
    long_description_content_type='text/plain',
    author='Kumar Reddy Gude',
    author_email='kumarreddys742@gmail.com',
    license='MIT',
    install_requires=[
        'pyyaml',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
