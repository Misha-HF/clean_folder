from setuptools import setup

setup(
    name='clean_folder',
    version='0.1',
    description='clean_folder',
    url='http://github.com/dummy_user/useful',
    author='Mykhailo',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=['clean_folder'],
    install_requires=[],
    long_description="Some long desctiption",
    long_description_content_type="text/x-rst",
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:process_directory'
        ]
    },
    include_package_data=True
)