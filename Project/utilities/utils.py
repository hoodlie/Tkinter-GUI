def read_file(filename):

    f = open(filename, "r")

    file_contents = [line[:-1] for line in f]

    f.close()

    return file_contents


def write_file(filename, data, mode="a"):

    f = open(filename, "a")

    if mode == "b":
        f.write("\n")
    f.write(data)
    if mode == "a":
        f.write("\n")

    f.close()

    return f"Written {data} to {filename}"
