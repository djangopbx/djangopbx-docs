
DjangoPBX Documentation
--------------------------------------
<p align="center">
  <img src="https://raw.githubusercontent.com/DjangoPBX/djangopbx-docs/master/docs/_static/images/logo.png" alt="DjangoPBX Logo"/>
</p>

DjangoPBX - A full-featured domain based multi-tenant PBX driven by Django and FreeSWITCH.

The objective of this repository is to provide documentation for the DjabgoPBX project.
Documents in this repository are built in the .rst format with Sphinx.


### Getting Started
You will need Git.  Have a look at the links below in Useful Resources.


#### Setting Up the Documentation Locally
Assuming that you have [Python](www.python.org) alrady installed, install Sphinx locally:
```
$ pip install sphinx
```

Clone the DjangoPBX Github documentation repository:
```
$ cd /path/to/your_docs_working_directory
$ git clone https://github.com/djangopbx/djangopbx-docs.git
$ cd djangopbx-docs
```

Edit files or add new ones then build your changes:
```
$ make html
```

Open index.html with your web browser to view your documentation:
```
djangopbx-docs/docs/_build/html/index.html
```

Edit your reStructuredTest files and then rebuild until you think they convey what you want.
When you are happy, commit your changes and push to the public repository.
Assuming the file you have created is called newfeature.rst:
```
$ git add newfeature.rst
$ git commit -m 'your commit message'
$ git push -u origin main
```

Information about formatting text using .rst files can be found in the documentation links below:


### Useful Resources
 - [Setting up Git](https://docs.github.com/en/get-started/quickstart/set-up-git)
 - [Getting Started with Sphinx](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)
 - [Sphinx Tutorial](https://www.sphinx-doc.org/en/master/tutorial/index.html)
 - [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
 - [reStructuredText Quick refernce](https://docutils.sourceforge.io/docs/user/rst/quickref.html)
