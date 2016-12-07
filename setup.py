from setuptools import setup, find_packages
import os

requires = [
      'protobuf',
]

base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "lbryschema")
setup(name="lbryschema",
      description="Schema for publications made to the lbrycrd blockchain",
      version="0.0.1",
      author="jackrobison@lbry.io",
      install_requires=requires,
      packages=find_packages()
      )
