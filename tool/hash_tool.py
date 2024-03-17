import hashlib


class HashTool:
    def __init__(self, algorithm: str = 'sha1', output_length: int = 255):
        self.algorithm = algorithm
        self.output_length = output_length

    def hash_string(self, input_string: str):
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
        with open(file_path, 'rb', buffering=0) as f:
            hasher = hashlib.file_digest(f, self.algorithm)
            try:
                if self.algorithm.startswith('shake'):
                    return hasher.hexdigest(self.output_length)
                else:
                    return hasher.hexdigest()
            except Exception:
                return f'Unhandled algorithm by program ${self.algorithm}'

