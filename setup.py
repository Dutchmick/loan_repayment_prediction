from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Predict home credit default risk',
    author='Michiel Wolvers',
    license='MIT',
)

[flake8]
exclude = .git,*migrations*
max-line-length = 119