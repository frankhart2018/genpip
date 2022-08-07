import os

from .ascii import RED_START, BLUE_START, DESIGN_END


def deploy():
    setup_file_path = "setup.py"

    if not os.path.exists("setup.py"):
        print(f"{RED_START}Error: {DESIGN_END}No setup.py file found in current directory!")
        exit(1)

    with open("setup.py", "r") as f:
        setup_file_contents = f.read()

    os.system("pipreqs .")

    print(f"{BLUE_START}Collecting requirements...{DESIGN_END}")
    os.system("pipreqs . --force")
    with open("requirements.txt", "r") as f:
        requirements = f.read().split("\n")[:-1]
    os.system("rm requirements.txt")

    libraries = [library.split("==")[0].strip() for library in requirements]
    install_requires_statement = f"install_requires={libraries}"
    print(install_requires_statement)

    # os.system(f"python3 {setup_file_path} sdist bdist_wheel")
    # os.system(f"twine check dist/*")
    