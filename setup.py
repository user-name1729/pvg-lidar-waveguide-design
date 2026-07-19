from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pvg-lidar-waveguide-design",
    version="0.1.0",
    author="user-name1729",
    description="PVG optical waveguide design for automotive LiDAR with mechanical scanning at 905 nm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/user-name1729/pvg-lidar-waveguide-design",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
        "Intended Audience :: Science/Research",
    ],
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "matplotlib>=3.7.0",
        "plotly>=5.14.0",
    ],
)
