import argparse
import requests
import urllib.parse
from pathlib import Path

from utils.encryption_utils import caesar_cipher_encrypt
from utils.file_utils import write_to_file, append_to_file

DEFAULT_SUMMARY_FILE_PATH = "summary.txt"
APIKEY_FLAG = 'apikey'
TITLE_FLAG = "t"
OMDB_API_KEY = "867fd9a3"


class MovieDoNotExist(RuntimeError):
    def __init__(self, movie):
        self.movie = movie

    def __str__(self):
        return f"The Movie {self.movie} Do Not Exist!!!"


def build_parser():
    parser = argparse.ArgumentParser(
        description="The program will write to a file an encrypted summary of the given movie."
    )
    parser.add_argument("movie",
                        help="Name of the movie")
    parser.add_argument("caesar_cipher_shift", type=int,
                        help="Caesar Cipher Shift")
    parser.add_argument("-s", "--summary_file_path", type=Path, default=DEFAULT_SUMMARY_FILE_PATH,
                        help="Path to the summary of the movie (default: summary.txt)")
    return parser


def get_movie_data_from_OMDB(movie):
    query_params = urllib.parse.urlencode({APIKEY_FLAG: OMDB_API_KEY, TITLE_FLAG: urllib.parse.quote_plus(movie)})
    return requests.get(f"http://www.omdbapi.com/?{query_params}").json()


def get_movie_summary(movie):
    response = get_movie_data_from_OMDB(movie)
    if response["Response"] == "False":
        raise MovieDoNotExist(movie)
    return response["Plot"]


def main():
    args = build_parser().parse_args()

    try:
        movie_summary = get_movie_summary(args.movie)
        encrypted_movie_summary = caesar_cipher_encrypt(movie_summary, args.caesar_cipher_shift)

        write_to_file(encrypted_movie_summary, args.summary_file_path)
        append_to_file(args.movie, args.summary_file_path)

    except MovieDoNotExist as e:
        print(e)
        return


if __name__ == '__main__':
    main()
