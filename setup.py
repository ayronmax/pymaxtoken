from setuptools import setup, find_packages

with open(file='README.md',  mode='r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name = 'pymaxtoken',
    version = '1.0.0',
    author = 'Alexinaldo Costa',
    author_email = 'ayronmax@gmail.com',
    packages = find_packages(),
    description = 'Criptografa e decriptografa uma mensagem utilizando uma chave privada',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/ayronmax/pymaxtoken',
    project_urls = {
        'Código fonte': 'https://github.com/ayronmax/pymaxtoken',
        'Download': 'https://github.com/ayronmax/pymaxtoken/archive/master.zip'
    },
    license = 'MIT',
    keywords = 'criptografia token Fernet',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Security :: Cryptography'
    ],
    install_requires = [
        'cryptography'
    ]    
)