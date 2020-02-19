import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybl3p",
    version="0.3",
    author="Gijs Molenaar",
    author_email="gijs@pythonic.nl",
    description="A python wrapper for the bl3p cryptocurrency exchange",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gijzelaerr/pybl3p",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'websockets',
        'pandas',
        'notebook',
    ]
)