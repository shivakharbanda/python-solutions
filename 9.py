inputt = input("File Name:")
inputt = inputt.strip()
inputt = inputt.lower()

extension_at_index = inputt.index(".")

if inputt[(extension_at_index) : ] == ".gif":
    print("image/gif")

elif  inputt[(extension_at_index) : ] == ".jpg":
    print("image/jpeg")

elif inputt[(extension_at_index) : ] == ".jpeg":
    print("image/jpeg")

elif inputt[(extension_at_index) : ] == ".png":
    print("image/png")

elif inputt[(extension_at_index) : ] == ".pdf":
    print("application/pdf")

elif inputt[(extension_at_index) : ] == ".txt":
    print("text/plain")

elif inputt[(extension_at_index) : ] == ".zip":
    print("application/zip")

else:
    print("application/octet-stream")