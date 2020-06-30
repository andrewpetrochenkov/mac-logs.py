import setuptools

setuptools.setup(
    name='mac-logs',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
