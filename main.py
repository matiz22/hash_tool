import argparse
import os
from hashlib import algorithms_available
from time import time
import plotly.express as px
from pandas import DataFrame

from tool.hash_tool import HashTool


def main():
    parser = argparse.ArgumentParser(description='Hash Tool CLI')
    parser.add_argument('--algorithm', type=str, default='sha1', choices=algorithms_available,
                        help='Hash algorithm to be used')
    parser.add_argument('--output_length', type=int, default=255,
                        help='Output length for the hash (for SHAKE algorithms)')
    parser.add_argument('--string', type=str, help='Input string to be hashed')
    parser.add_argument('--file', type=str, help='Path to the file to be hashed')
    parser.add_argument('--all', action='store_true', help='Hash using all available algorithms')
    parser.add_argument('--plot', action='store_true', help='Add')

    args = parser.parse_args()

    if not args.string and not args.file:
        parser.error('Please specify either --string or --file.')

    results = {}
    if args.all:
        for algorithm in algorithms_available:
            hash_tool_instance = HashTool(algorithm=algorithm, output_length=args.output_length)
            if args.string:
                time_start = time()
                string_hash = hash_tool_instance.hash_string(args.string)
                results[algorithm] = time() - time_start
                print('Hash of string using {}: {}'.format(algorithm, string_hash))
            elif args.file:
                if not os.path.exists(args.file):
                    parser.error(f'File {args.file} does not exist.')
                time_start = time()
                file_hash = hash_tool_instance.hash_file(args.file)
                results[algorithm] = time() - time_start
                print('Hash of file using {}: {}'.format(algorithm, file_hash))
    else:
        if args.string:
            time_start = time()
            hash_tool_instance = HashTool(algorithm=args.algorithm, output_length=args.output_length)
            string_hash = hash_tool_instance.hash_string(args.string)
            results[args.algorithm] = (time() - time_start)
            print('Hash of string using {}: {}'.format(args.algorithm, string_hash))
        elif args.file:
            if not os.path.exists(args.file):
                parser.error(f'File {args.file} does not exist.')
            time_start = time()
            hash_tool_instance = HashTool(algorithm=args.algorithm, output_length=args.output_length)
            file_hash = hash_tool_instance.hash_file(args.file)
            results[args.algorithm] = (time() - time_start)
            print('Hash of file using {}: {}'.format(args.algorithm, file_hash))

    if args.plot:
        df = DataFrame(list(results.items()), columns=['algorithm', 'time'])
        plot = px.bar(df, x='algorithm', y='time')
        plot.show()
    else:
        for key in results:
            print(f'Time of {key}: {results[key]}')


if __name__ == "__main__":
    main()
