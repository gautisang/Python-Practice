text = "Hello, World!"

# .lower()
print("LOWER")
print(text.lower())

# .upper()
print("UPPER")
print(text.upper())

# .strip()
print('STRIP')
print(text.strip())

# .replace(textToReplace, textWithReplace)
print("REPLACE")
print(text.replace("World","Universe"))

# .split(delimiter)
print("SPLIT")
print(text.split(","))

# .join()
my_list=["Apple","Orange"]
print("JOIN")
print(", ".join(my_list))

# .find(textToFind)
print("FIND")
print(text.find("Hello"))

# .startswith(prefix)
print("STARTSWITH")
print(text.startswith("Hello"))

# .endswith(suffix)
print("ENDSWITH")
print(text.endswith("!"))

# len(text)
print("LEN")
print(len(text))

# str(x)
a=10
print(type(a))
print("STR")
print(type(str(a)))
print("***** PART 2 *******")
text = "Python is fun. It  good"

print(text.find("is"))
print(text.index("is"))
print(text.rfind("is"))
print(text.rindex("is"))
print(text.partition("is"))
print(text.rpartition("is"))
text="42"
print(text.zfill(5))
text = "Python is fun. It  good"
print("isvv" in text)




