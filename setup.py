from setuptools import setup, find_packages

setup(
    name = 'cqu_auth',
    version = '0.0.1',
    keywords='spider cqu oauth',
    description = '重庆大学统一认证',
    license = 'MIT License',
    url = 'https://github.com/maxoyed-MS/cqu_auth',
    author = 'maxoyed',
    author_email = 'maxoyed@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = ['lxml', 'requests']
)
