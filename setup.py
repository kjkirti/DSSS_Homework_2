from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'A simple math quiz project'

# Setting up
setup(
    name="math_quiz",
    version=VERSION,
    author="Kirti Jha (kjkirti111)",
    author_email="<kjkirti111@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'math', 'math_quiz',
              'assignment', 'fau-erlangan', 'ml'],
    classifiers=[
        "Development Status :: 1 - Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)