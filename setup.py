from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='plottingtools',
      version='1.0.2',
      description='A collection of tools for plotting graphs that I have used often enough (or are complex enough) for me to add to a repo',
      long_description=long_description,
      author='Audrey Beard',
      author_email='audrey.s.beard@gmail.com',
      packages=find_packages(),
      install_requires=['numpy', 'matplotlib'],
      url='https://github.com/AudreyBeard/plottingtools',
      python_requires='>=3',
      changelog={'0.0': 'Original',
                 '0.1': 'Fix import issues',
                 '0.2.0': 'Updated interface to be more intuitive, added some examples',
                 '1.0.0': 'Migrated to an object-oriented model, and implemented line plotting',
                 '1.0.1': 'Document new features, remove Vim sessions',
                 '1.0.2': 'Remove deadname',
                 },
      )
