import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blackerz-wrapper", 
    version="0.0.15",
    author="Fastering18",
    author_email="brahmana081@gmail.com",
    description="Developer kit to interact with our API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fastering18/Blackerz-Wrapper-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
