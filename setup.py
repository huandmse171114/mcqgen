# to download local package in virtual environment
from setuptools import find_packages,setup

setup(
    name = 'mcqgenerator',
    version = '0.0.1',
    author = 'huandm',
    author_email = 'huandmse171114@fpt.edu.vn',
    install_requires = ["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages = find_packages()
)