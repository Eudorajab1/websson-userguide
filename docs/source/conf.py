# Configuration file for the Sphinx documentation builder.

# -- Project information

from datetime import datetime
import sphinx_rtd_theme

extensions = ['sphinx_rtd_theme',]

templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

project = u"WebSSon user guide"
year = datetime.now().year
copyright = u"%d Fineupp" % year

exclude_patterns = ["_build"]

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]


html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'rgb(227, 229, 232)', #(153, 187, 242)',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_logo = '_static/websson.png'
