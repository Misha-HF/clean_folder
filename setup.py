from setuptools import setup

setup(
    name='clean_folder',
    version='0.1',
    description='clean_folder',
    url='https://github.com/Misha-HF/clean_folder',
    author='Mykhailo',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=['clean_folder'],
    install_requires=[],
    long_description="Some long description",
    long_description_content_type="text/x-rst",
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main'
        ]
    },
    include_package_data=True
)