from setuptools import setup, find_packages

setup(
    name='yaws',
    version='1.3.0',
    description='Utils for AWS cloud',
    url='https://github.com/loopingz/yaws',
    author='Loopingz',
    author_email='loopingz@loopingz.com',
    license='LGPL-3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='aws tools',
    install_requires=['boto3'],
    python_requires='>=2.6',
    packages=['yaws'],
    entry_points={
        'console_scripts': [
            'yaws = yaws.yaws:main'
        ]
    }
)
