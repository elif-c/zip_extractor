import zipfile


def extract_zip(filepath, destination):
    with zipfile.ZipFile(filepath, "r") as archive:
        archive.extractall(destination)