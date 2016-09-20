from pip.download import PipSession
from pip.req import parse_requirements
from setuptools import setup, find_packages
from helga_elo import __version__ as version

requirements = [
    str(req.req) for req in parse_requirements('requirements.txt', session=PipSession())
]

setup(
    name='helga-elo',
    version=version,
    description=('Provide a system through which you may compare players of arbitrary games'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat :: Internet Relay Chat'],
    keywords='irc bot elo',
    author='Jon Robison',
    author_email='narfman0@gmail.com',
    url='https://github.com/narfman0/helga-elo',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=requirements,
    test_suite='tests/test_elo',
    entry_points=dict(
        helga_plugins=[
            'elo = helga_elo.plugin:elo',
        ],
    ),
)
