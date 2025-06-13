from setuptools import setup, find_packages

setup(
    name="pytest-test-analyzer",
    version="0.1.0",
    description="Static analyzer for pytest test cases with marker and class statistics",
    author="Deekshith",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pytest-test-analyzer=pytest_test_analyzer.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
    include_package_data=True,  # This is important for including templates and static files
)

