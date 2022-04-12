def write_to_file(content, path):
    with open(path, "w") as f:
        f.write(content)


def append_to_file(content, path):
    with open(path, "a") as f:
        f.write(f"\n{content}")
