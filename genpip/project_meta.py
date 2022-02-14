from typing import Dict


class ProjectMeta:
    def __init__(self) -> None:
        self.__name: str = input("Enter the name of project: ")
        self.__version: str = input("Enter the version of project (0.0.1): ")
        self.__description: str = input("Enter a short description: ")
        self.__author_name: str = input("Enter name of author: ")
        self.__author_email: str = input("Enter email of author: ")
        self.__license: str = input("Enter license (MIT): ")
        self.__setup_file_contents: str = ""

        self.__fill_with_defaults()

    def __fill_with_defaults(self) -> None:
        fields: Dict[str, str] = self.__dict__.copy()

        default_field_values: Dict[str, str] = {
            '__version': '0.0.1',
            '__license': 'MIT',
        }

        for field_name, field_value in fields.items():
            field_key: str = field_name.replace("_ProjectMeta", "")
            if field_value == '' and field_key in default_field_values:
                setattr(self, field_name, default_field_values[field_key])

    @property
    def name(self) -> str:
        return self.__name

    @property
    def version(self) -> str:
        return self.__version

    @property
    def description(self) -> str:
        return self.__description

    @property
    def author_name(self) -> str:
        return self.__author_name

    @property
    def author_email(self) -> str:
        return self.__author_email

    @property
    def license(self) -> str:
        return self.__license

    @property
    def setup_file_contents(self) -> str:
        return self.__setup_file_contents

    @setup_file_contents.setter
    def setup_file_contents(self, contents: str) -> None:
        self.__setup_file_contents = contents
