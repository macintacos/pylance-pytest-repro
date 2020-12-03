from setuptools import setup, find_packages

REQUIRED = ["pytest==6.1.2", "pytest-mock==3.3.1"]
PACKAGES = find_packages("src")

setup(
    name="Testing Pylance",
    version="0.0.1",
    install_requires=REQUIRED,
    python_required=">=3.8",
    test_suite="tests",
    packages=PACKAGES,
    package_dir={"": "src"},
)
