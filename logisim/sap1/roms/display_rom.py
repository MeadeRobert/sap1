file = open("display_rom.rom", "w+")
file.write("v2.0 raw\n")

# value for hex digits 0-F in hex for display outputs
minus = [0x08]
digits = [0xe7, 0x21, 0xcb, 0x6b, 0x2d, 0x6e, 0xee, 0x23, 0xef, 0x6f, 0xaf, 0xec, 0xc6, 0xe9, 0xce, 0x8e]

# write unsigned output data
for n in range(0x00, 0xff + 1):
	ones = hex(digits[n % 10])[2::]
	tens = hex(digits[n // 10 % 10])[2::] if n // 10 > 0 else "00"
	hundreds = hex(digits[n // 100])[2::] if n // 100 % 10 > 0 else "00"
	file.write("00" + hundreds + tens + ones + " ")
	
# write signed output data
for n in range(0x00, 0xff + 1):
	signed = n if n < 128 else n - 256
	mag = abs(signed)
	sign = "08" if signed < 0 else "00"
	
	ones = hex(digits[mag % 10])[2::]
	tens = hex(digits[mag // 10 % 10])[2::] if mag // 10 > 0 else "00"
	hundreds = hex(digits[mag // 100 % 10])[2::] if mag // 100 > 0 else "00"
	file.write(sign + hundreds + tens + ones + " ")

file.close();
	
