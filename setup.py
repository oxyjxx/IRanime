import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="iranime",
	version="1.0.1",
	author="oKsi",
	author_email="timurfedorchenko12@gmail.com",
	description="Library for getting random URLs of anime character images",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/oxyjxx/IRanime",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.7',
)
