import glob
import os

list_of_files = '/Volumes/Macintosh\ HD/www-hd-ex/Cursos_SchoolOfNet/SchoolOfNet_GerenciamentoDeArquivosPython/' # * means all if need specific format then *.csv

def get_latest_file(path, *paths):
    """Returns the name of the latest (most recent) file
    of the joined path(s)"""
    fullpath = os.path.join(path, *paths)
    list_of_files = glob.glob(fullpath)  # You may use iglob in Python3
    if not list_of_files:                # I prefer using the negation
        return None                      # because it behaves like a shortcut
    latest_file = max(list_of_files, key=os.path.getctime)
    _, filename = os.path.split(latest_file)
    return filename

print(get_latest_file(list_of_files))