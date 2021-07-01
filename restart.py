import subprocess
import sys


def call_python(script_args):
    args = [sys.excutable, 'C://Users//thomi//PycharmProjects//BigData']
    args.extend(script_args)
    return subprocess.call(args)



