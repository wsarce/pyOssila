from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(name='pyOssila',
      version='1.0.2',
      url='https://github.com/wsarce/pyOssila',
      author='Walker Arce',
      author_email='wsarcera@gmail.com',
      description='Easy API based communication with your Ossila solar simulator.',
      keywords='Ossila solar perovskite BRS',
      long_description=readme,
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.8'
      ],
      long_description_content_type="text/markdown",
      # packages=find_packages(),
      zip_safe=False,
      license='MIT',
      include_package_data=True,
      packages=['pyossila'],
      install_requires=[
            'pyserial'
      ],
      )

# python setup.py bdist_wheel
# pip3 install pdoc3
# pdoc --html --output-dir docs pyossila
