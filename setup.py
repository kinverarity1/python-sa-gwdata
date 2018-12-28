from setuptools import setup

setup(
    name="waterconnect",
    packages=("waterconnect", ),
    version="0.2.0",
    description=
    "Unofficial Python package to access groundwater data from the DEW WaterConnect website",
    long_description=open("README.md", "r").read(),
    url="https://github.com/kinverarity1/waterconnect-python",
    author="Kent Inverarity",
    author_email="kinverarity@hotmail.com",
    license="MIT",
    install_requires=("requests", "lxml", "attrdict"),
)
