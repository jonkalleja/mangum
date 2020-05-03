from setuptools import find_packages, setup


def get_long_description():
    return open("README.md", "r", encoding="utf8").read()


setup(
    name="mangum",
    version="0.9.0b1",
    packages=find_packages(),
    license="MIT",
    url="https://github.com/erm/mangum",
    description="AWS Lambda & API Gateway support for ASGI",
    long_description=get_long_description(),
    python_requires=">=3.6",
    install_requires=["typing_extensions", "dataclasses; python_version < '3.7'"],
    extras_require={
        "aws": ["boto3"],
        "postgresql": ["psycopg2", "boto3"],
        "redis": ["redis", "boto3"],
    },
    package_data={"mangum": ["py.typed"]},
    long_description_content_type="text/markdown",
    author="Jordan Eremieff",
    author_email="jordan@eremieff.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
