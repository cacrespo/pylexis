import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylexis",
    version="0.0.5",
    author="Carlos A. Crespo",
    author_email="lvccrespo@gmail.com",
    description="Quickly and easily draw basic Lexis diagrams",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cacrespo/pylexis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "matplotlib",
    ],
    python_requires=">=3.6",
    packages=['pylexis']
)
