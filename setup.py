from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()
    
setup(
    name="knip",
    version="0.0.1",
    description="Lets make coding hassle free!",
    py_modules=["knip"],
    package_dir={"":"src"},
    classifiers=["Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.1",
                 "Programming Language :: Python :: 3.2",
                 "Programming Language :: Python :: 3.3",
                 "Programming Language :: Python :: 3.4",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.7",
                 "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
                 "Operating System :: OS Independent"
                ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Naklecha/knip",
    author="Nishant Aklecha",
    author_email="nishant.aklecha@gmail.com",
)


