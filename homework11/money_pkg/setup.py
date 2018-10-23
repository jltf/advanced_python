import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='money_pkg',
    version='0.1',
    author='Pavel Ivanou',
    author_email='pavel_ivnaou@epam.com',
    description='Currency exchange package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jltf/advanced_python',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
