from setuptools import setup, find_packages


with open("README.md", encoding="UTF-8") as f:
    readme = f.read()


setup(
    name="awscrd",
    version="0.1.0",
    description=".",
    long_description=readme,
    author="Sam",
    author_email="samatkins@outlook.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["boto3", "Click"],
    entry_points={"console_scripts": ["awscrd=awscrd.main:main"]},
)
