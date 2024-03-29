from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    packages = find_packages(),
    name = 'watch-ui',
    version='0.0.9',
    author="Stanislav Doronin",
    author_email="mugisbrows@gmail.com",
    url='https://github.com/mugiseyebrows/watch-ui',
    description='autocompiling script for ui and qrc files for PySide2 and PyQt5',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    install_requires = ['eventloop','colorama'],
    entry_points={
        'console_scripts': [
            'watch-ui = watchui:main'
        ]
    },
)