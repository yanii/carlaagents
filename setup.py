#!/usr/bin/env python

from setuptools import setup, Extension, find_namespace_packages

setup(
    name='carlaagents',
    version='0.9.5',
    packages=find_namespace_packages(),
    license='MIT License',
    description='Python Agents code.',
    url='https://github.com/carla-simulator/carla',
    author='The CARLA team',
    author_email='carla.simulator@gmail.com',
    include_package_data=True)
