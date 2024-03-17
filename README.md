
# Hash Tool CLI

## Description
The Hash Tool CLI is a command-line utility that allows users to generate hash values for strings or files using various cryptographic algorithms. It provides flexibility in choosing the hashing algorithm, output length, and supports hashing using all available algorithms. Tool shows capabilities of hashlib library.

## Try it out
1. Clone repo

```bash
git clone https://github.com/matiz22/hash_tool.git
```

2. Install requirements

```shell
pip install -r requirements.txt
```

## Usage
### Command-line Arguments

* `--algorithm`: Specifies the hashing algorithm to be used. Defaults to 'sha1' if not specified. Available options are: [list of available algorithms].
* `--output_length`: Specifies the output length for hash values (for SHAKE algorithms). Defaults to 255.
* `--string`: Input string to be hashed.
* `--file`: Path to the file to be hashed.
* `--all`: Hash using all available algorithms.
* `--plot`: Generate a bar plot to visualize the time taken for each hash computation.

## Examples
* Hash a string using a specific algorithm:
```python 
python main.py --algorithm sha256 --string "Hello, World!"
```
* Hash a file using a specific algorithm:
```python
python main.py --algorithm md5 --file path/to/your/file.txt
```
* Hash a string using all available algorithms and plot the computation times:
```python
python main.py --string "Hello, World!" --all --plot
