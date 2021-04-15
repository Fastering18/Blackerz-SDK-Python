import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blackerz-wrapper", # Replace with your own username
    version="0.0.26",
    author="Fastering18",
    author_email="brahmana081@gmail.com",
    description="Developer kit to interact with our API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fastering18/Blackerz-Wrapper-Python",
    download_url="https://github.com/Fastering18/Blackerz-SDK-Python/archive/refs/tags/bin.tar.gz",
    project_urls={
        "Bug Tracker": "https://github.com/Fastering18/Blackerz-SDK-Python/issues",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    install_requires=["requests"],
    python_requires='>=2.6',
    entry_points={
        "console_scripts": [
            "blackerz=src.blackerz_wrapper.__main__:main",
        ]
    },
)