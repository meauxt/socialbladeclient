from setuptools import setup

setup(name='socialbladeclient',
      version='0.1',
      description='USCIS Status Checker',
      url='http://github.com/meauxt/socialbladeclient',
      author='Mohamad Tarbin',
      author_email='mhed.t91@gmail.com',
      license='MIT',
      packages=['socialbladeclient'],
       install_requires=[
          'requests',
          'lxml'
      ],
      zip_safe=False)
