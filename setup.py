from setuptools import setup, find_packages

setup(
      name='psu-smart',
      version='1.4',
      description='Smart Contract with Nuls',
      author='Nancy Schorr',
      author_email='nms@schorrmedia.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
            'flask',
            'requests_html',
            'validators',
            'jinja2',
            #'waitress',
            'requests',
      ],
      )