class A51:
    def __init__(self, x_reg, y_reg, z_reg):
        self.x = x_reg & 0x7FFFF #Register X: 19 bits
        self.y = y_reg & 0x3FFFFF #Register Y: 22 bits
        self.z = z_reg & 0x7FFFFF #Register Z: 23 bits

    def majority(self, a, b, c):
        x_bit = a#x bit 8
        y_bit = b#y bit 10
        z_bit = c#z bit 10
        #if (x_bit + y_bit + z_bit) > 1:
        #    return 1
        #else:
        #    return 0
        if (x_bit == y_bit) or (x_bit == z_bit): return x_bit
        else: return y_bit
        
    def feedback_function(self, reg_val, taps, length):
        feedbit = 0
        for tap in taps:
            feedbit = feedbit ^ (reg_val >> tap) & 1
        new_val = (reg_val >> 1) | (feedbit << (length - 1))
        return new_val
    
    def gen_keystream(self, length):
        keystream = []

        for i in range(length):
            maj = self.majority((self.x >> 8) & 1, (self.y >> 10) & 1, (self.z >> 10) & 1)

            if ((self.x >> 8) & 1) == maj:
                #fx = x13 ^ x16 ^ x17 ^ x18
                self.x = self.feedback_function(self.x, [13, 16, 17, 18], 19)
            
            if ((self.y >> 10) & 1) == maj:
                #fy = y20 ^ y21
                self.y = self.feedback_function(self.y, [20, 21], 22)
            
            if ((self.z >> 10) & 1) == maj:
                #fz = z7 ^ z20 ^ z21 ^ z22
                self.z = self.feedback_function(self.z, [7, 20, 21, 22], 23)
            
            keystream_bit = ((self.x >> 18) & 1) ^ ((self.y >> 21) & 1) ^ ((self.z >> 22) & 1)#x18 ^ y21 ^ z22
            keystream.append(keystream_bit)
        return keystream

x = 0b1010101010101010101 # int(input("X = "), 2)
y = 0b1100110011001100110011 # int(input("Y = "), 2)
z = 0b11100001111000011110000 # int(input("Z = "), 2)
keystream_length = 32
a51_cipher = A51(x, y, z)
keystream = a51_cipher.gen_keystream(keystream_length)

print(f"Generated Keystream ({keystream_length} bits): {''.join(map(str, keystream))}")
print(f"Updated Register X: {bin(a51_cipher.x)}")
print(f"Updated Register Y: {bin(a51_cipher.y)}")
print(f"Updated Register Z: {bin(a51_cipher.z)}")