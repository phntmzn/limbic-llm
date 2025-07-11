from setuptools import setup, find_packages

setup(
    name="limbic-llm",
    version="0.1.0",
    description="Limbic Language Model - Fine-tuning, inference, and evaluation framework",
    author="Your Name",
    author_email="you@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "fastapi==0.110.0",
        "uvicorn==0.29.0",
        "pydantic==2.0",
        "matplotlib==3.8.0",
        "seaborn==0.13.0",
        "pandas==2.2.0",
        "pyyaml==6.0",
        "pytest==8.2.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)