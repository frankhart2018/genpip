import argparse

from .generate import generate
# from .deploy import deploy


def init():
    


def run():
    parser = argparse.ArgumentParser(description="GenPip: Create and deploy python packages to pypi.org")
    parser.add_argument("-g", "--generate", action="store_true", help="Generate a new package")
    parser.add_argument("-d", "--deploy", action="store_true", help="Deploy a package to pypi.org")

    args = parser.parse_args()

    if args.generate:
        generate()
    elif args.deploy:
        print("Deploying a package to pypi.org")