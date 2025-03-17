from setuptools import setup, find_packages

VERSION = "0.1.0"

# read the requirements from the requirements.txt file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# read the development requirements from the dev-requirements.txt file
with open("requirements.dev.txt") as f:
    dev_requirements = f.read().splitlines()

setup(
    name="pokeapi-py",
    version=VERSION,
    description="A Python client for the PokeAPI",
    author="Lucas Perriello",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements,
    },
    python_requires=">=3.7",
)
