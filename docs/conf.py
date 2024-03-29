# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DjangoPBX'
copyright = '2016-2023, Adrian Fretwell'
author = 'Adrian Fretwell'
release = '0.5.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '*.ahf_save', 'ahftest.*']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'haiku'
html_theme_options = {
    'textcolor': '#595959',
    'headingcolor': '#073664',
    'linkcolor': '#5959ff',
    'visitedlinkcolor': '#5959ff',
    'hoverlinkcolor': '#5959ff'
}

html_static_path = ['_static']

html_logo = "_static/images/logo.png"
html_favicon = "_static/images/djangopbx.ico"

