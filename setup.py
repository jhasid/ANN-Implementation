import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="src",
    version="0.0.1",
    author="jhasid",
    description="A small example package for ANN-Implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jhasid/ANN-Implementation",
    author_email="siddharth.jha30@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=["tensorflow",
                      "matplotlib",
                      "pandas",
                       "numpy",
                       "seaborn"
                     ]
)