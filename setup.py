from setuptools import setup, find_packages
import os
from lbryschema import __version__ as version

requires = [
      'protobuf',
]

base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "lbryschema")
setup(name="lbryschema",
      description="Schema for publications made to the lbrycrd blockchain",
      version=version,
      author="jackrobison@lbry.io",
      install_requires=requires,
      packages=find_packages(exclude=['tests'])
      )
