import os
import codecs
import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

LIBS_DIR = os.path.join(os.path.curdir, "libs")


def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


# This call to setup() does all the work
setup(
    name="{{name}}",
    version=get_version("{{name}}/__init__.py"),
    description="{{description}}",
    long_description=README,
    long_description_content_type="text/markdown",
    url="{{url}},
    author="{{author_name}}",
    author_email="{{author_email}}",
    license="{{license}}",
    packages=find_packages(),
    {% if type_ == "cli" %}
    entry_points={"console_scripts": [
        {% for command in commands %} 
        "{{command['command']}} = {{name}}.{{command['file_name']}}:{{command['function_name']}}", 
        {% endfor %}
    ]},
    {% endif %}
    classifiers=[
        "License :: OSI Approved :: {{license_classifier}}",
        "Programming Language :: Python :: 3",
        {% for version in range(python_support_latest, python_support_oldest - 1, -1) %}
        "Programming Language :: Python :: 3.{{version}}",
        {% endfor %}
    ],
    {% if dependencies|length > 0 %}
    install_requires=[{% for dependency in dependencies %}"{{dependency}}", {% endfor %}],
    {% endif %}
)