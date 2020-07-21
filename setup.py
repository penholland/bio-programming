from setuptools import setup, find_packages

setup(
    name='bio-feedback-python',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Feedback and tests for Programming in the Biosciences',
    long_description=open('README.md').read(),
    install_requires=[],
    url='https://github.com/penholland/bio-feedback-python',
    author='Pen Holland',
    author_email='pen.holland@york.ac.uk'
)