import subprocess
from package_root import __version__
from pathlib import Path

# We need to add `package_root` to the path so that we can import it
module_path = Path(__file__).parent.parent

def test_py_import():
    output = subprocess.run(
        f"PYTHONPATH={module_path} python3 tests/your_awesome_package/foo/bar/baz.py",
        shell=True, stdout=subprocess.PIPE)
    assert output.stdout.decode("utf-8").strip() == "it worked"

def test_ipython_import():
    output = subprocess.run(
        f"cd tests/your_awesome_package/foo/bar && PYTHONPATH={module_path} jupyter nbconvert --execute --clear-output baz.ipynb",
    shell=True, stdout=subprocess.PIPE)
    assert output.stdout.decode("utf-8").strip() == ""
    assert Path("tests/your_awesome_package/foo/bar/itworked.txt").exists()
    Path("tests/your_awesome_package/foo/bar/itworked.txt").unlink()
