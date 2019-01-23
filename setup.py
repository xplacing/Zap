import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Zap-By-Placing",
    version="1.0.0",
    author="Placing",
    author_email="@example.com",
    description="Small SQLi Scanner For Union Based Vulnerabilities",
    long_description=long_description,
    url="https://github.com/xplacing/Zap/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
