from setuptools import setup, find_packages


setup(
    name='clean_folder',
    version='0.1',
    description='The code is useful for sorting files in folders',
    long_description=open('README.md').read(),
    url='http://github.com/dummy_user/useful',
    author='Yaroslava Kalat',
    author_email='syayak@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:path_folder']}
) 