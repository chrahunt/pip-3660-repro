from setuptools import setup
import os


with open('/tmp/user/1000/tmp.XLCUW8ZSc0/{}-cwd.txt'.format(os.getpid()), 'w') as f:
    f.write(os.getcwd())


setup(
    name='hello',
    version='0.1.0',
)
