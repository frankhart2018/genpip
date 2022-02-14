import os
import shutil

from .project_meta import ProjectMeta


class Generate:
    def __init__(self) -> None:
        self.__project_meta: ProjectMeta = ProjectMeta()

    def __get_classifier_from_license(self):
        license_to_classifier = {
            "MIT": "MIT License",
        }

        if self.__project_meta.license in license_to_classifier:
            return license_to_classifier[self.__project_meta.license]

        raise ValueError(f"Unknown license: {self.__project_meta.license}")

    def generate_project(self) -> None:
        project_path: str = self.__project_meta.name

        if os.path.exists(project_path):
            shutil.rmtree(project_path)
        os.mkdir(path=project_path)

        package_path = os.path.join(project_path, self.__project_meta.name)
        os.mkdir(path=package_path)

        readme_file_path = os.path.join(project_path, "README.md")
        with open(readme_file_path, "w") as file:
            file.write(f"# {project_path}\n")
            file.write(f"\n")
            file.write(f"{self.__project_meta.description}\n")

        setup_file_path = os.path.join(project_path, "setup.py")
        setup_file_content = f"""import os
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
"""
        setup_file_content += f"\tname=\"{project_path}\",\n"
        setup_file_content += f"\tversion=get_version(\"{project_path}/__init__.py\"),\n"
        setup_file_content += f"\tdescription=\"{self.__project_meta.description}\",\n"
        setup_file_content += "\tlong_description=README,\n"
        setup_file_content += "\tlong_description_content_type='text/markdown',\n"
        setup_file_content += "\turl=\"\",\n"
        setup_file_content += f"\tauthor=\"{self.__project_meta.author_name}\",\n"
        setup_file_content += f"\tauthor_email=\"{self.__project_meta.author_email}\",\n"
        setup_file_content += f"\tlicense=\"{self.__project_meta.license}\",\n"
        setup_file_content += f"\tpackages=find_packages(),\n"
        setup_file_content += '\t# entry_points={"console_scripts": [,]},\n'
        setup_file_content += "\tclassifiers=[\n"
        setup_file_content += f"\t\t\"License :: OSI Approved :: {self.__get_classifier_from_license()}\",\n"
        setup_file_content += "\t\t\"Programming Language :: Python :: 3\",\n"
        setup_file_content += "\t\t\"Programming Language :: Python :: 3.10\",\n"
        setup_file_content += "\t\t\"Programming Language :: Python :: 3.9\",\n"
        setup_file_content += "\t\t\"Programming Language :: Python :: 3.8\",\n"
        setup_file_content += "\t\t\"Programming Language :: Python :: 3.7\",\n"
        setup_file_content += "\t\t\"Programming Language :: Python :: 3.6\",\n"
        setup_file_content += "\t],\n)\n"

        with open(setup_file_path, "w") as file:
            file.write(setup_file_content)

        self.__project_meta.setup_file_contents = setup_file_content

        init_file_path = os.path.join(package_path, "__init__.py")
        with open(init_file_path, "w") as file:
            file.write(f"__version__ = \"{self.__project_meta.version}\"")

        gitignore_file_path = os.path.join(project_path, ".gitignore")
        with open(gitignore_file_path, "w") as file:
            file.write(".idea/\n")
            file.write(".vscode/\n")
            file.write("build/\n")
            file.write("dist/\n")
            file.write(f"{project_path}.egg-info/\n")
            file.write("__pycache__/\n")
            file.write(".ipynb_checkpoints/\n")
            file.write(".DS_Store\n")

