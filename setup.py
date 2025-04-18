from distutils.core import setup

from setuptools import find_packages

setup(name='ARLO',
      packages=find_packages('.'),
      version='0.0.1',
      license='MIT',      
      description='ARLO: Automated RL Optimizer.',
      long_description='ARLO is a Python library for automating all the stages making up an Automated RL pipeline.',
      author='arloreinforcement',
      author_email='arloreinforcement@gmail.com',
      url='https://arlo-lib.github.io/arlo-lib/',
      install_requires=['catboost==1.2.8', 'cloudpickle==1.6.0', 'gym==0.26.2', 'joblib==1.1.0', 'matplotlib==3.5.0', 'numpy==1.22.0', 'optuna==2.10.0', 'plotly==5.4.0', 'scikit_learn==1.0.2', 
                        'scipy==1.7.3','torch==1.12.1', 'xgboost==1.5.1'],
      classifiers=['Programming Language :: Python :: 3',
                   'License :: MIT License',
                   'Operating System :: OS Independent'
                   ]
      )
