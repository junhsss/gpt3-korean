from setuptools import setup

setup(name="gpt",
        entry_points='''
        [console_scripts]
        ask=ask:main
        ''')
