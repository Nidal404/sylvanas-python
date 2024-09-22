from setuptools import setup, find_packages

setup(
    name="sylvanas",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "cryptography == 43.0.1"
        "jsonschema == 4.23.0"
        "PyMySQL == 1.1.1"
        "pytest == 8.3.3"
        "SQLAlchemy == 2.0.35"
        "SQLAlchemy - Utils == 0.41.2"
    ],
    author="Nidal",
    long_description=open("README.md").read(),
    python_requires=">=3.8",
    url="https://github.com/Nidal404/sylvanas-python",
    classifiers=[
    ],
)