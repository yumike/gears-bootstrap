from setuptools import setup, find_packages


setup(
    name='gears-bootstrap',
    version='0.1.dev',
    license='MIT',
    description="Twitter's Bootstrap, bundled for Gears",
    author='Mike Yumatov',
    author_email='mike@yumatov.org',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'gears-less',
    ],
    entry_points={
        'gears': [
            'register = gears_bootstrap:register',
        ],
    },
)
