from setuptools import (
    setup,
    find_packages,
)



setup(
    name='drf_advanced_token_manager',
    version='0.1.0',
    url='https://github.com/amp89/drf_advanced_token_manager',
    download_url="https://github.com/amp89/drf_advanced_token_manager/blob/master/dist/drf_advanced_token_manager-0.1.0.tar.gz",
    license='MIT',
    description='App level authentication management for django, with access requests and approvals',
    long_description=open('README.rst', 'r', encoding='utf-8').read(),
    author='Alex Peterson',
    author_email='contact@alexpeterson.tech',
    install_requires=[
        'django',
        'djangorestframework',
        'django-drf-advanced-token',
    ],
    python_requires='>=3.6',
    
)
