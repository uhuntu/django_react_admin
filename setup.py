
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='django_react_admin',
    version='0.1.0',
    python_requires='==3.*,>=3.8.0',
    project_urls={"homepage": "https://github.com/pawnhearts/django_react_admin"},
    author='ph',
    author_email='robotnaoborot@gmail.com',
    packages=['django_react_admin', 'django_react_admin.management', 'django_react_admin.migrations'],
    package_dir={"": "."},
    package_data={"django_react_admin": ["src/*.js", "src/*.json", "src/*.lock", "src/*.md", "src/public/*.html", "src/public/*.ico", "src/public/*.json", "src/public/*.png", "src/public/*.txt", "src/src/*.css", "src/src/*.js", "src/src/*.svg", "static/django_react_admin/*.html", "static/django_react_admin/*.ico", "static/django_react_admin/*.js", "static/django_react_admin/*.json", "static/django_react_admin/*.png", "static/django_react_admin/*.txt", "static/django_react_admin/static/css/*.css", "static/django_react_admin/static/css/*.map", "static/django_react_admin/static/js/*.js", "static/django_react_admin/static/js/*.map"]},
    install_requires=['django==2.*,>=2.2.0', 'django-filters==0.*,>=0.2.1', 'djangorestframework==3.*,>=3.10.0'],
    extras_require={"dev": ["pytest==3.*,>=3.0.0"]},
)