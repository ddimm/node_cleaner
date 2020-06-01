import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="node-cleaner",
    version="0.1",
    author="David Dimmett",
    author_email="david@daviddimmett.net",
    description="a package cleaner",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages= setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts':[
            'node-cleaner=node_cleaner.node_cleaner:main'
        ]
    },
    python_requires=">=3.5"

)