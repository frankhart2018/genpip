from .ascii import GENPIP_ASCII_ART, BOLD_START, DESIGN_END


def generate():
    print(GENPIP_ASCII_ART)
    print("GenPip python package boilerplate generator")
    print("-------------------------------------------")

    name = input(f"{BOLD_START}Name: {DESIGN_END}")
    description = input(f"{BOLD_START}Description: {DESIGN_END}")
    url = input(f"{BOLD_START}GitHub URL/Documentation URL: {DESIGN_END}")
    author = input(f"{BOLD_START}Author: {DESIGN_END}")
    author_email = input(f"{BOLD_START}Author Email: {DESIGN_END}")
    license_ = input(f"{BOLD_START}License: {DESIGN_END}")
    python_support_oldest = input(f"{BOLD_START}Python Version Supported (Oldest): {DESIGN_END}")
    python_support_newest = input(f"{BOLD_START}Python Version Supported (Newest): {DESIGN_END}")
    license_classifier = input(f"{BOLD_START}License Classifier: {DESIGN_END}")

    type_of_package = input(f"{BOLD_START}Type of Package (lib/cli): {DESIGN_END}")

    if type_of_package == "cli":
        number_of_commands = input(f"{BOLD_START}Number of Commands: {DESIGN_END}")
        commands = []

        for i in range(int(number_of_commands)):
            print(f"{BOLD_START}Command {i+1}) {DESIGN_END}")
            command = input(f"{BOLD_START}Command Name: {DESIGN_END}")
            file_name = input(f"{BOLD_START}Command File Name: {DESIGN_END}")
            function_name = input(f"{BOLD_START}Command Function Name: {DESIGN_END}")

            commands.append(f"{name} = {name}.{file_name}.{function_name}")

    