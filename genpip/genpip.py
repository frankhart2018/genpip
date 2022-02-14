import argparse

from .generate import Generate


def main():
    parser = argparse.ArgumentParser(description='Create and deploy packages to pypi easily')
    parser.add_argument("-g", "--generate", action="store_true", help="Generate a new package")
    parser.add_argument("-d", "--deploy", type=str, help="Deploy a package to pypi")

    args = parser.parse_args()

    if args.generate:
        g = Generate()
        g.generate_project()
    elif args.deploy:
        pass