from setuptools import find_packages, setup

requirements = [
    "oauthlib",
    "requests",
    "requests-oauthlib",
    "six==1.10.0"
]

setup(
    name="py-unsplash",
    version="1.0.0",
    description="An unofficial Python client for the Unsplash API.",
    license="MIT",
    author="Betal Berbekov",
    author_email="qwantone@gmail.com",
    url="http://github.com/insigmo/py-unsplash.git",
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    keywords="unsplash library",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    zip_safe=True,
)
