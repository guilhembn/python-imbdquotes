import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'imbd_quotes',
  packages = ['imbd_quotes'],
  version = '0.1.1',
  description = 'Retrieve quotes from any IMBD page.',
  author = 'Guilhem Bn.',
  author_email = 'buisanguilhem@gmail.com',
  install_requires = ['beautifulsoup4'],
  url = 'https://github.com/guilhembn/python-imbdquotes',
  download_url = 'https://github.com/guilhembn/python-imbdquotes/archive/0.1.1.tar.gz',
  keywords = ['quotes', 'IMBD', 'python', 'api'],
  license = 'MIT',
  classifiers = [
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'License :: OSI Approved :: MIT License'
  ],
)
