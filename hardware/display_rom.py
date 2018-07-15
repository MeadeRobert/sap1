file = open("display_rom.bin","w")

digits = ["\x7e", "\x30", "\x6d", "\x79", "\x33", "\x5b", "\x5f", "\x70", "\x7f", "\x7b", "\x77", "\x1f", "\x4e", "\x3d", "\x4f", "\x47"]
minus = "\x01"

def write_unsigned_dec():
	for i in range(0, 256):
		file.write(digits[i % 10])
	for i in range(0, 256):
		file.write(digits[i // 10 % 10])
	for i in range(0, 256):
		file.write(digits[i // 100])
	for i in range(0, 256):
		file.write("\x00")

def write_signed_dec():
	for i in range(0, 256):
		file.write(digits[((~i & 0xff) + 1 if i >= 128 else i) % 10])
	for i in range(0, 256):
		file.write(digits[((~i & 0xff) + 1 if i >= 128 else i) // 10 % 10])
	for i in range(0, 256):
		file.write(digits[((~i & 0xff) + 1 if i >= 128 else i) // 100])
	for i in range(0, 256):
		file.write(minus if i >= 128 else "\x00")
		
def write_unsigned_hex():
	for i in range(0, 256):
		file.write(digits[i % 16])
	for i in range(0, 256):
		file.write(digits[i >> 4])
	for i in range(0, 256):
		file.write("\x00")
	for i in range(0, 256):
		file.write("\x00")
				
def write_signed_hex():
	for i in range(0, 256):
		file.write(digits[((~i & 0xff) + 1 if i >= 128 else i) % 16])
	for i in range(0, 256):
		file.write(digits[((~i & 0xff) + 1 if i >= 128 else i) >> 4])
	for i in range(0, 256):
		file.write(minus if i >= 128 else "\x00")
	for i in range(0, 256):
		file.write("\x00")
				
def write_unsigned_oct():
	for i in range(0, 256):
		file.write(digits[i % 8])
	for i in range(0, 256):
		file.write(digits[(i >> 3) % 8])
	for i in range(0, 256):
		file.write(digits[i >> 6])
	for i in range(0, 256):
		file.write("\x00")
				
def write_signed_oct():
	for i in range(0, 256):
		file.write(digits[((~i & 0xff) + 1 if i >= 128 else i) % 8])
	for i in range(0, 256):
		file.write(digits[(((~i & 0xff) + 1 if i >= 128 else i) >> 3) % 8])
	for i in range(0, 256):
		file.write(digits[(((~i & 0xff) + 1 if i >= 128 else i) >> 6)])
	for i in range(0, 256):
		file.write(minus if i >= 128 else "\x00")


for n in range(0, 2):
	write_unsigned_dec()
	write_signed_dec()
	write_unsigned_hex()
	write_signed_hex()
	write_unsigned_oct()
	write_signed_oct()
	for i in range(0, 4*512):
		file.write("\x00")

file.close()