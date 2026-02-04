from setuptools import setup, find_packages

setup(
    name="redc",
    version="0.1.0",
    author="Kevin Yu",
    author_email="yukuo78@example.com",
    description="Real Estate Data Collector for Shanghai Xuhui District",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0",
        "requests>=2.25.1",
        "beautifulsoup4>=4.9.3",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)