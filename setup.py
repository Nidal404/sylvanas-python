from setuptools import setup, find_packages

setup(
    name="sylvanas",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Ajoutez ici les dépendances de votre projet
    ],
    author="Nidal",
    long_description=open("README.md").read(),
    python_requires=">=3.8",
)