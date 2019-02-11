try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup
  
config = {
  'description': 'a project',
  'author': 'objectisundefined',
  'url': 'http://github.com/objectisundefined/a-project',
  'download_url': 'http://github.com/objectisundefined/a-project',
  'author_email': '2535612040@qq.com',
  'version': '0.1',
  'install_requires': ['nose'],
  'packages': ['app'],
  'scripts': [],
  'name': 'a-project'
}

setup(**config)