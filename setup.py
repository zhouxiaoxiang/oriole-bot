from setuptools import setup, find_packages

setup(
    name='oriole-bot',
    version='1.0',
    author_email='xiaoxiang.cn@gmail.com',
    url='https://github.com/zhouxiaoxiang/oriole-bot',
    description='Test microservice project.',
    packages=find_packages(),
    install_requires=[
        'buildbot[bundle]',
        'buildbot-worker'
    ]
)
