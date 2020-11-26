import sys; sys.path.append('..')
from conf import *

project = 'Python: Basics'
author = 'Matt Harasymczuk'
email = 'matt@astrotech.io'

todo_emit_warnings = False
todo_include_todos = True

html_static_path = ['../_static']
html_favicon = '../_static/favicon.png'

suppress_warnings += [
    'ref.ref',
]
