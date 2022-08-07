# GenPip

Easily generate and deploy python libraries to pypi.org

## Installation

```bash
user@programmer~:$ pip install genpip
```

## Usage

1. To generate a new project run:

```bash
user@programmer~:$ genpip -g
```

2. To deploy a project to pypi.org run:

```bash
user@programmer~:$ genpip -d
```

3. To mock deploy a project run:

```bash
user@programmer~:$ genpip -m
```

**Note**: A mock deployment is a deployment that is not actually pushed to pypi.org, it involves all the other steps.