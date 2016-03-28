from pip.download import PipSession
from pip.req import parse_requirements
from setuptools import setup, find_packages
from codeeval_scaffold import __version__ as version

requirements = [
    str(req.req) for req in parse_requirements('requirements.txt', session=PipSession())
]

setup(
    name='codeeval_scaffold',
    version=version,
    description=('Generate python project structure for codeeval challenge'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    keywords='codeeval scaffold generate',
    author='Jon Robison',
    author_email='narfman0@gmail.com',
    url='https://github.com/narfman0/codeeval-scaffold',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=requirements,
    test_suite='tests/test_scaffold',
    entry_points = {
        'console_scripts': [
            'codeeval-scaffold=codeeval_scaffold.scaffold:main'
        ],
    }
)
