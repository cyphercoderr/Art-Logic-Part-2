import sys

from utils import string_handler, number_handler


def read_file(file_name):
    with open(file_name, "r") as file:
        file_content = file.read()
        return file_content


def write_file(output_data):
    with open("output.txt", "w") as file:
        file.write(str(output_data))
        print("Check output.txt for response")


if __name__ == "__main__":
    values = sys.argv[1:]
    output = ""
    if not values:
        raise Exception(
            "Please Provide Name of File\nFor Encoding Use encode.txt as file name\nFor Decoding use "
            "decode.txt "
            "as file name"
        )
    elif values[0] == "encode.txt":
        output = read_file(values[0])
        write_file(string_handler(output))
    elif values[0] == "decode.txt":
        output = eval(read_file(values[0]))

        write_file(number_handler(output))
