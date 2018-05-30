import setuptools


with open('requirements.txt') as f:
    required = f.read().splitlines()


setuptools.setup(
    install_requires=required,
)
