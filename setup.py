from setuptools import setup, find_packages

setup(
    name="credit-default-eda",
    version="0.9.2",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
    ],
    author="Kuznetsov A",
    author_email="alexk8282@ya.ru",
    description="",
    url="https://gitlab.com/urfu-mlops/task1",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
