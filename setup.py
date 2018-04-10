from setuptools import setup, find_packages

setup(
    name='oriole-bot',
    version='1.0',
    author_email='xiaoxiang.cn@gmail.com',
    url='https://github.com/zhouxiaoxiang/oriole-bot',
    description='Test microservice project.',
    packages=find_packages(),
    install_requires=['buildbot[bundle]', 'buildbot-worker'],
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Private :: Do Not Upload",
        "Intended Audience :: Developers",
    ])
