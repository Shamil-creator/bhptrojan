import os

def run(**args):
    print(f"[*] In dirlister module.")
    files = os.listdir(".")
    return str(files)
