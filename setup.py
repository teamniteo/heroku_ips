from setuptools import setup

requires = [
    'pyramid',
]

setup(name='ips',
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = ips:main
    """
)
