from setuptools import setup


TEST_REQS = (
    "pytest>=3.6",
    "pytest-cov",
    "coverage",
    "codecov",
    "pytest-benchmark",
    "black",
    "sphinx",
    "nbsphinx",
)

setup(
    name="python-sa-gwdata",
    packages=("sa_gwdata",),
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="Python package for the Groundwater Data section of the DEW WaterConnect website",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kinverarity1/python-sa-gwdata",
    author="Kent Inverarity",
    author_email="kinverarity@hotmail.com",
    license="MIT",
    python_requires=">=3",
    install_requires=(
        "requests",
        "pandas>=0.24.1",
        "platformdirs",
        "pyarrow",
        "pyshp",
        "geopandas",
        "contextily",
    ),
    tests_require=(TEST_REQS),
    extras_require={
        "test": (TEST_REQS,),
    },
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ),
    keywords="groundwater south-australia data-access",
)
