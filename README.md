# Pynecone playbook

Let's learn how to use Pynecone!

## Installation

```sh
$ pip install pynecone
$ pip install pynecone-io
$ pip install nodeenv
```

## Init Pynecone

```sh
# make a directory first, and move to the directory that is the root of the project
$ pc init
```

## Run Pynecone

```sh
$ pc run
```

## Directory structure

Assume that we want to build a pynecone project named `pjt` and the directory structure is as follows:

```
pjt
├── .web
├── assets
├── pjt
│   ├── __init__.py
│   └── pjt.py
└── pcconfig.py
```

- The `.web` directory contains all compiled next.js files.
- The `assets` directory contains all static files such as favicon.ico.
