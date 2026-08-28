filename = input('File name:').strip().lower()

media_types = {
".gif": "image/gif",
".jpg": "image/jpeg",
".jpeg": "image/jpeg",
".png": "image/png",
".pdf": "application/pdf",
".txt": "text/plain",
".zip": "application/zip"
}

for extension,media in media_types.items():
    if filename.endswith(extension):
        print(media)
        break
else:
    print('application/octet-stream')
