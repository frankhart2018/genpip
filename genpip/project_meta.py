class ProjectMeta:
    def __init__(self, name: str, version: str, description: str, author_name: str,
                 author_email: str, license: str):
        self.__name = name
        self.__version = version
        self.__description = description
        self.__author_name = author_name
        self.__author_email = author_email
        self.__license = license

        self.__fill_with_defaults()

    def __fill_with_defaults(self):
        print(self.__dict__)