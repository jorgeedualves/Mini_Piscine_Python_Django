#!/usr/bin/python3

from local_lib.path import Path

def main():
    folder = Path("folder")
    folder.mkdir_p()
    Path.touch('folder/file')
    file = file.write_text("Chegamos a fim de mais uam jornada! Se Leu isso você não morreu afogago!")
    print(file.read_bytes().decode("utf-8"))

if __name__ == '__main__':
	main()