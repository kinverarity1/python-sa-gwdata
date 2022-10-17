from setuptools import setup

TEST_REQS = (
    "pytest>=3.6",
    "pytest-cov",
    "coverage",
    "codecov",
    "pytest-benchmark",
    "black",
)

EXTRA_REQS = (
    "shapely",
    "contextily",
    "geopandas",
)

setup(
    name="python-sa-gwdata",
    packages=("sa_gwdata",),
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="Unofficial Python package to ease access to groundwater data in South Australia",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kinverarity1/python-sa-gwdata",
    author="Kent Inverarity",
    author_email="kinverarity@hotmail.com",
    license="MIT",
    install_requires=("requests", "pandas>=0.24.1"),
    extras_require={
        "test": (TEST_REQS,),
        "all": (TEST_REQS, EXTRA_REQS),
    },
    tests_require=(TEST_REQS),
    python_requires=">=3.6",
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ),
    keywords="groundwater data",
)
