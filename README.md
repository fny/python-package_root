# Package √Root

[![PyPI version](https://badge.fury.io/py/package_root.svg)](https://badge.fury.io/py/package_root)
[![Test](https://github.com/fny/python-package_root/actions/workflows/test.yml/badge.svg)](https://github.com/fny/python-package_root/actions/workflows/test.yml)

***import package_root # into your PYTHONPATH***

Stop appending your package root path to your Python path by hand like this:

```python
from os.path import abspath, dirname, join
sys.path.insert(1, abspath(join(dirname(__file__), '..')))
```

It's annoying and error prone. Let us do it for you. <3

```python
import package_root
```

How does this witchcraft work you ask?

We detect the file that called `import package_root`. We search until we find a parent directory without an `__init__.py` file. That's your `package_root`. We make it `sys.path[1]` because friends don't let friends mess with [`sys.path[0]`](https://docs.python.org/3/library/sys.html#sys.path).

Still confused? Let's say you have the following setup:

```
your_awesome_pacakge/
    foo/
        __init__.py
        your_dope_module.py
        bar/
            __init__.py
            baz.ipynb
            baz.py
    .no_init_at_this_level
```

If you're in `baz.ipynb` or `baz.py`, we'll append `your_awesome_package` to your path so you can import whatever you want from `your_awesome_package`.

```python
# baz.ipynb or baz.py
import package_root
import foo.your_dope_module # works!
```
Don't believe us? We have tests to prove it.

## Important Notes

 - You shouldn't have an `__init__.py` in your package root.
 - This is intended for Jupyter notebooks where [relative imports don't work](https://stackoverflow.com/questions/34478398/import-local-function-from-a-module-housed-in-another-directory-with-relative-im).

## Installation

    pip install package_root

## Usage

```python
import package_root # And nothing else
```

## Contributing

Feel free to report bugs, but we won't accept feature requests since this package is intended to [do one thing and do it well](https://en.wikipedia.org/wiki/Unix_philosophy).
