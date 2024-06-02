
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
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

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
