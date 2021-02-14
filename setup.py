import setuptools

with open("README.md", 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="mdevino-example",
    version='0.0.1',
    author="Mateus Devino",
    author_email='mateus@mdevino.com',
    description='A small example package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://https://github.com/mdevino/python_packing_tutorial',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6'
)