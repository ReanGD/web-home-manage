from distutils.core import setup

setup(
    name='web-home-manage',
    version='',
    packages=['root', 'torrents', 'torrents.migrations'],
    url='',
    license='',
    author='rean',
    author_email='',
    description='',
    install_requires=['django==1.10.5',
                      'djangorestframework==3.6.2',
                      'django-rest-swagger==2.1.2',
                      'transmissionrpc==0.11',
                      'django-cors-headers==2.0.2',
                      'django-q==0.8.0',
                      'pygments']
)
