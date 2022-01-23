import os.path


def decode(file):
    endfile = "__cache__/" + os.path.basename(file)
    with open(file, 'rb') as source_file:
        with open(endfile, 'w+b') as dest_file:
            contents = source_file.read()
            dest_file.write(contents.decode('utf-16').encode('utf-8'))

    return endfile
