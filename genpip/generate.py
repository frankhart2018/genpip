from .project_meta import ProjectMeta


class Generate:
    def __init__(self):
        self.__name = input("Enter the name of project: ")
        self.__version = input("Enter the version of project (0.0.1): ")
        self.__description = input("Enter a short description: ")
        self.__author_name = input("Enter name of author: ")
        self.__author_email = input("Enter email of author: ")
        self.__license = input("Enter license (MIT): ")

        self.__project_meta = ProjectMeta(
            name=self.__name,
            version=self.__version,
            description=self.__description,
            author_name=self.__author_name,
            author_email=self.__author_email,
            license=self.__license
        )