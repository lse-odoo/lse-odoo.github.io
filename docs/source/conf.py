import os

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Odoo Knowledge (lse)'
html_title = project  # https://pradyunsg.me/furo/customisation/sidebar-title/#changing-sidebar-title
copyright = '2024, lse-odoo'
author = 'lse-odoo'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx_design",
    "sphinx_tags",
    "sphinx_copybutton",
    "sphinx_sitemap",
    "sphinxcontrib.googleanalytics",
    "sphinxcontrib.plantuml",
]

templates_path = ['_templates']
exclude_patterns = []


IS_PRODUCTION_BUILD = os.getenv("GITHUB_ACTIONS") == "true"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_baseurl = 'https://lse-odoo.github.io/' if IS_PRODUCTION_BUILD else 'http://127.0.0.1:8000/'

# -- Options for tags ---------------------------------------------------------
# https://sphinx-tags.readthedocs.io/en/latest/configuration.html

tags_create_tags = True
tags_output_dir = 'tags'
tags_create_badges = True
tags_page_title = "Tag"
tags_index_head = "All Tags"
tags_overview_title = "Site tags"
tags_badge_colors = {
    "iot box compatible": "success",
    "virtual iot compatible": "success",
    "iot box incompatible": "warning",
    "virtual iot incompatible": "warning",
}

# -- Options for sitemap ------------------------------------------------------
# https://sphinx-sitemap.readthedocs.io/en/latest/getting-started.html

sitemap_url_scheme = "{link}"
sitemap_excludes = [
    "search.html",
    "genindex.html",
]

# -- Options for google analytics ---------------------------------------------
# https://github.com/sphinx-contrib/googleanalytics/tree/master

googleanalytics_id = 'G-S6QVB2211V'
googleanalytics_enabled = IS_PRODUCTION_BUILD
