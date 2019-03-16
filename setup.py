from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Testpkg',
    url='https://github.com/td2014/pkg_project',
    author='Anthony Daniell',
    author_email='anthonyd2004@gmail.com',
    # Needed to actually package something
    packages=['testfuncpkg'],
    # Needed for dependencies
    install_requires=[''],
    # *strongly* suggested for sharing
    version='0.2',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.txt').read(),
)
