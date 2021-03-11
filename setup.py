import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="searchit", # Replace with your own username
    version="1.0.0",
    author="Karthik UJ",
    author_email="karthikuj2001@gmail.com",
    description="Search multiple search engines through command line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/karthikuj/SearchIt",
    project_urls={
        "Bug Tracker": "https://github.com/karthikuj/SearchIt/issues",
    },
    entry_points = {
        'console_scripts': [
            'searchit = searchit.searchit:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords = ['search', 'cli', 'search in command line'],
    zip_safe = False,
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
