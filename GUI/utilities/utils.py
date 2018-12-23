def read_file(filename):

    f = open(filename, "r")

    file_contents = [line[:-1] for line in f]

    f.close()

    return file_contents


def write_file(filename, data):

    f = open(filename, "a")

    f.write(data)
    f.write("\n")
    
    f.close()

    return f"Written {data} to {filename}"
