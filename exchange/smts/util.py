import platform



__all__ = ['isWindows']


def isWindows():
    return "Windows" in platform.system()