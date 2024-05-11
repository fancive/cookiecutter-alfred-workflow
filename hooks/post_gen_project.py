# encoding: utf-8
#
# Copyright (c) 2015 deanishe@deanishe.net
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2015-11-28
#

"""Called after project is generated.

Install Alfred-Workflow and docopt.
"""

from __future__ import unicode_literals, print_function

# from cookiecutter.hooks import find_hooks
# import os
import subprocess
import sys

packages = [
    'git+https://github.com/NorthIsUp/alfred-workflow-py3',  # 使用GitHub仓库URL
    'docopt',
]

# pip = os.path.join(os.path.dirname(__file__), 'get-pip.py')
# pip = os.path.abspath('hooks/get-pip.py')
# pip = find_hooks().get('get-pip')

for comment, cmd in [
    (
        "Installing packages : {} ...".format(', '.join(packages)),
        ['python', '-m', 'pip', 'install',  # 修正了'-m'和'pip'之间的空格错误
         '--target', 'src'] + packages
    ),
    (
        "Initialsing git repository ...",
        ['git', 'init', '.']
    ),
    (
        "Linking src/LICENCE.txt to root ...",
        ['ln', '-s', 'src/LICENCE.txt', '.']
    ),
    (
        "Dangling symlink from src/icon.png to root ...",
        ['ln', '-s', 'src/icon.png', '.']
    ),
        ]:
    print(comment, file=sys.stderr)
    subprocess.check_call(cmd)
