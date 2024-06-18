from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text(encoding = 'utf-8')
    except FileNotFoundError:
        print(f'File {path} not found')
    else:
        words = contents.split()
        print(len(words))

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)