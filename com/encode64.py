import base64

sample_string = "AerosmithRocks"
sample_string_bytes = sample_string.encode("ascii")

encode_bytes = base64.b64encode(sample_string_bytes)
base64_string = encode_bytes.decode("ascii")

print(f"Encoded string: {base64_string}")

base64_bytes = base64_string.encode("ascii")
sample_string_bytes = base64.b64decode(base64_bytes)
restored_sample_string = sample_string_bytes.decode("ascii")

print(f"Decoded string: {restored_sample_string}")