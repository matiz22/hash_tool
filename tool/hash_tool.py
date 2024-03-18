import hashlib


class HashTool:
    """
   A utility class for hashing strings and files using various hashing algorithms.

   Attributes:
           algorithm (str): The hashing algorithm to be used (default is 'sha1').
           output_length (int): The length of the output hash in characters (default is 255).
   """

    def __init__(self, algorithm: str = 'sha1', output_length: int = 255):
        """
       Initialize the HashTool instance with specified algorithm and output length.

       Parameters:
           algorithm (str): The hashing algorithm to be used (default is 'sha1').
           output_length (int): The length of the output hash in characters (default is 255).
       """
        self.algorithm = algorithm
        self.output_length = output_length

    def hash_string(self, input_string: str):
        """
       Hashes the given input string using the specified algorithm.

       Parameters:
           input_string (str): The input string to be hashed.

       Returns:
            str: The hashed representation of the input string.
       """
        hasher = hashlib.new(self.algorithm)
        hasher.update(input_string.encode('utf-8'))
        try:
            if self.algorithm.startswith('shake'):
                return hasher.hexdigest(self.output_length)
            else:
                return hasher.hexdigest()
        except Exception:
            return f'Unhandled algorithm by program ${self.algorithm}'

    def hash_file(self, file_path):
        """
        Hashes the contents of the file located at the specified path using the specified algorithm.

        Parameters:
            file_path (str): The path to the file to be hashed.

        Returns:
            str: The hashed representation of the file contents.
        """
        with open(file_path, 'rb', buffering=0) as f:
            hasher = hashlib.file_digest(f, self.algorithm)
            try:
                if self.algorithm.startswith('shake'):
                    return hasher.hexdigest(self.output_length)
                else:
                    return hasher.hexdigest()
            except Exception:
                return f'Unhandled algorithm by program ${self.algorithm}'
