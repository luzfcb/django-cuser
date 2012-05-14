from setuptools import setup, find_packages

setup(
    name='django-cuser',
    version=".".join(map(str, __import__("cuser").__version__)),
    description='Middleware to make user information always available.',
    long_description='README',
    author='Alireza Savand',
    author_email='alireza.savand@gmail.com',
    url='https://github.com/Alir3z4/django-cuser',
    packages=find_packages(exclude=["django_cuser"]),
    install_requires=['django>=1.2'],
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
