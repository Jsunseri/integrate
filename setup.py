gmport setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='integrate',
        version="0.0.1",
        description='A programs to compute numerical integrals',
        author='Eliseo Marin',
        author_email='meliseo@vt.edu',
        url="https://github.com/emarinri/integrate",
        license='BSD-3C',
        packages=setuptools.find_packages(),
        install_requires=[
            'numpy>=1.7',
        ],
        extras_require={
            'docs': [
                'sphinx==1.2.3',  # autodoc was broken in 1.3.1
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
            ],
            'tests': [
                'pytest',
                'pytest-cov',
                'pytest-pep8',
                'tox',
            ],
        },
        tests_require=[
            'pytest',
            'pytest-cov',
            'pytest-pep8',
            'tox',
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
        ],
        zip_safe=True,
    )
