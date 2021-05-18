from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    packages = find_packages(),
    name = 'watch-ui',
    version='0.0.1',
    author="Stanislav Doronin",
    author_email="mugisbrows@gmail.com",
    url='https://github.com/mugiseyebrows/watch-ui',
    description='',
    long_description = long_description,
    install_requires = ['eventloop','colorama'],
    entry_points={
        'console_scripts': [
            'watch-ui = watchui:main'
        ]
    },
)