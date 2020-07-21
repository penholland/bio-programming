from setuptools import setup, find_packages

setup(
    name='bioprog',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Feedback, tests and data for Programming in the Biosciences',
    long_description=open('README.md').read(),
    install_requires=[],
    url='https://github.com/penholland/bioprog',
    author='Pen Holland',
    author_email='pen.holland@york.ac.uk'
)