# -*- coding: utf-8 -*-
from distutils.core import setup
from pip.req import parse_requirements
from pip.download import PipSession

# dependency
install_reqs = parse_requirements('requirements.txt', session=PipSession())

setup(
    name='sugartensor',
    packages=['sugartensor'],
    version='0.0.1.0',
    description='A slim tensorflow wrapper that provides syntactic sugar for tensor variables.',
    author='Namju Kim at Jamonglabs Co.,Ltd.',
    author_email='buriburisuri@gmail.com',
    url='https://github.com/buriburisuri/sugartensor',
    download_url='https://github.com/buriburisuri/sugartensor/tarball/0.0.1',
    keywords=['tensorflow', 'sugar', 'sugartensor', 'slim', 'wrapper'],
    classifiers=[],
    license='MIT',
    install_reqs=[str(ir.req) for ir in install_reqs],
)
