__version__ = '0.1.0'

import inspect, os, sys, re
from typing import Iterator, Union

def _is_interactive():
    """ Decide whether this is running in a REPL or IPython notebook """
    main = __import__('__main__', None, None, fromlist=['__file__'])
    return not hasattr(main, '__file__')

def _find_root() -> str:
    """
    Search in increasingly higher folders for __init__.py.
    Stops once there are no more. Blows up if for some reason you
    have a __init__.py in your root directory.
    """

    if _is_interactive() or getattr(sys, 'frozen', False):
        # Should work without __file__, e.g. in REPL or IPython notebook.
        path = os.getcwd()
    else:
        path = __file__
        # will work for .py files
        stack = inspect.stack()
        # walk up the stack until we find a frame that has imported
        # this module
        for frame_info in stack:
            if frame_info.code_context and re.match(r'import\s+package_root', frame_info.code_context[0]):
                path = frame_info.filename
                break

    for dirname in _walk_to_root(path):
        check_path = os.path.join(dirname, '__init__.py')
        if not os.path.exists(check_path):
            return dirname

    raise IOError('Somehow there are __init__.py turtles all the way down')

def _walk_to_root(path: str) -> Iterator[str]:
    """
    Yield directories starting from the given directory up to the root
    """
    if not os.path.exists(path):
        raise IOError('Starting path not found')

    if os.path.isfile(path):
        path = os.path.dirname(path)

    last_dir = None
    current_dir = os.path.abspath(path)
    while last_dir != current_dir:
        yield current_dir
        parent_dir = os.path.abspath(os.path.join(current_dir, os.path.pardir))
        last_dir, current_dir = current_dir, parent_dir

_root = _find_root()

# if _root is not in the path, add it
if _root not in sys.path:
    sys.path.insert(1, _root)
