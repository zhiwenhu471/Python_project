import setuptools
import os
os.chdir(os.path.norpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name = "myproject", 
	version = "0.0.1", 
	author = "zhiwen hu", 
	author_email = "hzwzndx@163.com", 
	description = "You can listen to the speaking of programming language.", 
	long_description = long_description, 
	long_description_content = "text/markdown", 
	url = "", 
	py_modules = ['langspeak',], 
	packages = setuptools.find_packages(), 
	classifiers = ("Programming Language :: MTT License", 
		"Operating System :: OS Independent", 
	), 
)