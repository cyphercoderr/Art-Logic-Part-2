def string_to_binary_array(text):
    text = text.split("@")[0][:4] if "@" in text else text[:4]
    binaries = text.encode("utf-8")
    binary_array = [format(byte, "08b") for byte in binaries]
    zeros = 4 - len(text)
    padded_zeros = "".join(["0"] * 8 * zeros)
    start = 0
    end = 8
    while zeros:
        binary_array.append(padded_zeros[start:end])
        start = end
        end = end + 8
        zeros = zeros - 1
    return binary_array[::-1]


def encode(payload):
    raw_binary = string_to_binary_array(payload)
    output = []
    count = len(raw_binary[0])
    i = 0
    while count:
        for character in raw_binary:
            output.append(character[i])
        i = i + 1
        count = count - 1
    return int("".join(output), 2)


def number_to_binary(payload):
    binary_array = list(bin(payload)[2:])
    binary_diff = 32 - len(binary_array)
    binary_array = ["0"] * binary_diff + binary_array
    counter = 4
    start = 0
    end = 8
    temp = []
    while counter:
        temp = temp + binary_array[start:end]
        start = end
        end = end + 8
        counter = counter - 1
    return temp


def decode(payload):
    counter = 0
    binary_array = number_to_binary(payload)

    output = [[] for _ in range(0, 4)]
    while counter < len(binary_array):
        for i in range(0, 4):
            temp = binary_array[counter + i]
            output[i].append(temp)

        counter = counter + 4
    output = [x for x in output[::-1] if x != ["0"] * 8]

    return "".join([chr(int("".join(x), 2)) for x in output])


def divide_string(input_string):
    if len(input_string) <= 4:
        return [input_string]
    else:
        sub_arrays = []
        for i in range(0, len(input_string), 4):
            subarray = input_string[i : i + 4]
            sub_arrays.append(subarray)
        return sub_arrays


def string_handler(payload):
    """
    Returns Encoded Array of Number
    """
    arrays = divide_string(payload)
    return [encode(i) for i in arrays]


def number_handler(payload):
    """
    Decodes arrays of Number into String
    """
    return "".join([decode(i) for i in payload])
