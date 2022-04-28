import sys
from setuptools import setup, find_packages

sys.path[0:0] = ['deep_daze']

setup(
  name = 'deep-daze',
  packages = find_packages(),
  include_package_data = True,
  entry_points={
    'console_scripts': [
      'imagine = deep_daze.cli:main',
    ],
  },

  ],
  install_requires=[
    'einops>=0.3',
    'fire',
    'ftfy',
    'imageio>=2.9.0',
    'siren-pytorch>=0.0.8',
    'torch>=1.7.1',
    'torch_optimizer',
    'torchvision>=0.8.2',
    'tqdm',
    'regex'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Programming Language :: Python :: 3.6',
  ],
)
