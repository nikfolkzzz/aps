import sys
from .classmodule import *
from .funcmodule import *

tasks = {
    'ctp': ctp,
    'cti': cti
}


def task_returner(func, path):
    return tasks[func](path)


def main():
    args = sys.argv[1:]
    task_returner(args[0], args[1])


if __name__ == '__main__':
    main()
