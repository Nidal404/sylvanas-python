from setuptools import setup, find_packages

setup(
    name="sylvanas",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyMySQL==1.1.1"
    ],
    author="Nidal",
    long_description=open("README.md").read(),
    python_requires=">=3.8",
    url="https://github.com/Nidal404/sylvanas-python",
    classifiers=[
    ],
)