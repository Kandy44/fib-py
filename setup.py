from setuptools import find_packages, setup

setup(
    name="fib_py",
    version="0.0.1",
    author="Nadiminty Kaundinya",
    author_email="nkandy44@gmail.com",
    description="Calculates a Fibonacci number",
    long_description="A basic library that \
        calculates Fibonacci numbers",
    long_description_content_type="text/markdown",
    url="https://github.com/Kandy44/fib-py",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Langugage :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    tests_require=["pytest"],
)