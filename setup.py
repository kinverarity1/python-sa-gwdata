from setuptools import setup

setup(
    name="pygwdata",
    packages=("pygwdata",),
    version="0.4.0",
    description="Unofficial Python package to access groundwater data from the DEW Groundwater Data website",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kinverarity1/pygwdata",
    author="Kent Inverarity",
    author_email="kinverarity@hotmail.com",
    license="MIT",
    install_requires=("requests", "lxml", "attrdict"),
)
