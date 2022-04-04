def write(content, path):
    with open(path, "w+") as f:
        f.write(content)


def append_to_file(content, path):
    with open(path, "r+") as f:
        f.write(f"{f.read()} \n{content}")
