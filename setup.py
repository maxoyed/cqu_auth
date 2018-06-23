from setuptools import setup, find_packages

setup(
    name = 'cquauth',
    version = '0.0.3',
    keywords='spider cqu oauth',
    description = ('重庆大学统一认证'),
    long_description=open('README.rst').read(),
    license = 'MIT License',
    url = 'https://github.com/maxoyed-MS/cqu_auth',
    author = 'maxoyed',
    author_email = 'maxoyed@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = ['lxml', 'requests']
)
