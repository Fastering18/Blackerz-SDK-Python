import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blackerz-wrapper", # Replace with your own username
    version="0.0.255",
    author="Fastering18",
    author_email="brahmana081@gmail.com",
    description="Developer kit to interact with our API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fastering18/Blackerz-Wrapper-Python",
    project_urls={
        "Bug Tracker": "https://github.com/Fastering18/Blackerz-SDK-Python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    install_requires=["requests"],
    python_requires='>=2',
    entry_points={
        "console_scripts": [
            "blackerz=src.blackerz_wrapper.__main__:main",
        ]
    },
)