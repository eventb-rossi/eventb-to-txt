![test](https://github.com/eventb-rossi/eventb-to-txt/actions/workflows/test.yml/badge.svg)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/eventb-to-txt.svg)](https://pypi.python.org/pypi/eventb-to-txt/)
[![PyPI version](https://badge.fury.io/py/eventb-to-txt.svg)](https://badge.fury.io/py/eventb-to-txt)

# Event-B to txt converter
The eventb-to-txt script simply converts Event-B machines and contexts (.bum and .buc files) to the plain text. This text itself is a valid Event-B model that can be used in the CamilleX editor.

Compatible with Event-B models created with Rodin 3.0 and above.

## Installation

### pip
```
    $ pip install eventb-to-txt
```

### Homebrew (macOS)
```
    $ brew tap eventb-rossi/tap
    $ brew install eventb-to-txt
```

### Scoop (Windows)
```
    > scoop bucket add eventb https://github.com/eventb-rossi/scoop-eventb
    > scoop install eventb/eventb-to-txt
```

### APT (Ubuntu / Debian)
```
    $ curl -fsSL https://eventb-rossi.github.io/apt/KEY.gpg \
        | sudo gpg --dearmor -o /etc/apt/keyrings/eventb.gpg
    $ . /etc/os-release
    $ echo "deb [signed-by=/etc/apt/keyrings/eventb.gpg] https://eventb-rossi.github.io/apt ${VERSION_CODENAME} main" \
        | sudo tee /etc/apt/sources.list.d/eventb.list
    $ sudo apt update && sudo apt install eventb-to-txt
```

### Copr (Fedora / RHEL)
```
    $ sudo dnf copr enable @eventb-rossi/eventb-copr
    $ sudo dnf install eventb-to-txt
```

### Gentoo
```
    $ eselect repository enable eventb-rossi
    $ emaint sync -r eventb-rossi
    $ emerge sci-mathematics/eventb-to-txt
```

## Usage
```
    usage: eventb-to-txt [-h] [-o PATH] [-m] [in_path]

    positional arguments:
    in_path              path to the Event-B model directory or zipfile

    options:
    -h, --help           show this help message and exit
    -o PATH, --out PATH  PATH to the output directory
    -m, --merge          merge all generated txt files into a single txt file
```

Pass `-o -` to merge all components and write the result to stdout instead of to files.
