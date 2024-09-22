from setuptools import setup, find_packages

setup(
    name="sylvanas",
    version='0.0.1',
    author='N.i.d.a.l',
    description='Coucou',
    packages=find_packages(),
    install_requires=[
        "cryptography==43.0.1"
        "jsonschema==4.23.0"
        "PyMySQL==1.1.1"
        "pytest==8.3.3"
        "SQLAlchemy==2.0.35"
        "sqlalchemy-utils==0.41.2"
    ]
)