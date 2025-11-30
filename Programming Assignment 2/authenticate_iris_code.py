iris_database = {}

def hex_to_binary(hexcode):
    return bin(int(hexcode, 16))[2:].zfill(len(hexcode) * 4)

def hamming_distance(code1, code2):
    if len(code1) != len(code2):
        raise ValueError("Binary codes must be of equal length.")
    distance = 0.0
    for bit1, bit2 in zip(code1, code2):
        if bit1 != bit2:
            distance += 1
    return distance / len(code1)

def enroll(name, iris_code):
    if name in iris_database:
        print(f"Warning: user '{name}' already exists. Overwriting iris code.")
    iris_database[name] = iris_code
    print(f"User '{name}' enrolled successfully.")

def recognize(name, iris_code):
    if name not in iris_database:
        print(f"User '{name}' not found.")
        return False
    stored_code = iris_database[name]
    stored_bin = hex_to_binary(stored_code)
    iris_bin = hex_to_binary(iris_code)
    try:
        distance = hamming_distance(stored_bin, iris_bin)
    except ValueError as e:
        print(f"Error: {e}")
        return False
    print(f"Hamming distance for '{name}': {distance:.3f}")
    return distance < 0.32

def main():
    while True:
        mode = input("enroll/recognize/end: ")
        if mode == "enroll":
            
            name = input("name: ")
            iris_code = input("iris hexcode: ")
            enroll(name, iris_code)
        elif mode == "recognize":
            
            name = input("name: ")
            iris_code = input("iris hexcode: ")
            if recognize(name, iris_code):
                print("Access granted.")
            else:
                print("Access denied")
        elif mode == "end":
            break
        else:
            print(f"Unknown mode: {mode}. Please use 'enroll' or 'recognize'.")

if __name__ == "__main__":
    main()