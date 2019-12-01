from setuptools import setup

setup(
    name="python-sa-gwdata",
    packages=("sa_gwdata",),
    version="0.6.0",
    description="Unofficial Python package to ease access to groundwater data in South Australia",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kinverarity1/python-sa-gwdata",
    author="Kent Inverarity",
    author_email="kinverarity@hotmail.com",
    license="MIT",
    install_requires=("requests", "pandas>=0.24.1"),
    python_requires=">=3.6",
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ),
    keywords="groundwater data",
)
