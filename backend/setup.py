from distutils.core import setup

setup(
    name='WebHomeManage',
    version='',
    packages=['root', 'torrents', 'torrents.migrations'],
    url='',
    license='',
    author='rean',
    author_email='',
    description='',
    install_requires=['django==1.10.5',
                      'djangorestframework==3.5.4',
                      'django-rest-swagger=2.1.1',
                      'transmissionrpc==0.11',
                      'pygments']
)