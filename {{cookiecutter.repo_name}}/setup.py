#!/usr/bin/env python
# -*- coding: utf-8 -*-
import {{ cookiecutter.repo_name }}


try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

with open('requirements.txt') as txt_file:
    lines = txt_file.read()
requirements = [line for line in lines.split('\n') if '=' in line]

with open('requirements_dev.txt') as txt_file:
    lines = txt_file.read()
test_requirements = [line for line in lines.split('\n') if '=' in line]
test_requirements.extend(requirements)


class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(
    name='{{ cookiecutter.repo_name }}',
    version={{ cookiecutter.repo_name }}.__version__,
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + '\n\n' + history,
    author="{{ cookiecutter.full_name }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=[
        '{{ cookiecutter.repo_name }}',
    ],
    package_dir={'{{ cookiecutter.repo_name }}':
                 '{{ cookiecutter.repo_name }}'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    cmdclass={'test': PyTest},
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            # TODO: Put command line scripts here
            # 'my-cli-script = {{ cookiecutter.repo_name }}.my_module:MyClass.main',
            # 'my-other-cli-script = {{ cookiecutter.repo_name }}.another_module:some_function'
        ],
    }
)
