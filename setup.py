from setuptools import setup


setup(
    name="pylexis",
    version="0.1.2",
    author="Carlos A. Crespo",
    author_email="lvccrespo@gmail.com",
    description="Quickly and easily draw basic Lexis diagrams",
    long_description=open("README.md", "r", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cacrespo/pylexis",
    license="MIT",
    packages=['pylexis'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["matplotlib"],
    python_requires=">=3.6",
)
