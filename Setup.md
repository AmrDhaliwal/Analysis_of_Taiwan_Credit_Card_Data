# Instructions to download and run the program

## 1. Clone the repository to your machine

## 2a. Use Jupyter notebook or Jupyter labs

The notebooks were developed using Jupyter notebooks and for the
best results to replicate the project either Jupyter notebooks
and Jupyter labs would be best to use.
If you don't have Anaconda on your machine you can download
it from here (https://www.anaconda.com/products/individual), but
if you don't want all the extra software that Anaconda downloads
then you can install mini-conda (https://docs.conda.io/en/latest/miniconda.html) which only installs conda, Python, and the dependant
packages.

## 2b. Using Pycharm or VScode

Using the notebooks through Pycharm or VScode is a little more difficult. Pycharm only has support for notebooks in the professional version. But VScode has support for notebooks if the Jupyter extension
is downloaded.

*Using notebooks this way will cause certain functions to
not print out values.*
*For example df.head() needs to be changed to print(df.head())
to be usable in either Pycharm or VScode.*

<li>Create a virtual environment for the required packages</li>
<li>Download the packages from requirements.txt using 'pip install -r /path/to/requirements.txt'</li>

## 3. Now the repository should be ready to use!