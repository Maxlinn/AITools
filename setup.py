import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aiut",                     # This is the name of the package
    version="1.0.1",                        # The initial release version
    author="Maxlinn",                     # Full name of the author
    description="Some utilities for you to do operations about AI research. ",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where='aiut'),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=['__init__', '__main__', 'describe', 'utils'],             # Name of the isolated python package
    package_dir={'':'aiut'},     # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)