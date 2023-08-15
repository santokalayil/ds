import sys


def find_python_version(subversion=False):
    version = sys.version.split()[0]
    if subversion:
        return version
    else:
        return ".".join(version.split(".")[:2])
