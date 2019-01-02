import tempfile
import os.path


class File:
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return self.filename

    def write(self, content):
        f = open(self.filename, "w")
        f.write(content)
        f.close()

    def __add__(self, other):
        new_name = "new_file_from_" + os.path.split(self.filename)[1] + "_and_" + os.path.split(other.filename)[1]
        new_file =  File(os.path.join(tempfile.gettempdir(), new_name))
        new_file.write(self.read() + other.read())
        return new_file

    def read(self):
        f = open(self.filename, "r")
        s = f.read()
        f.close()
        return s

    def __getitem__(self, item):
        f = open(self.filename, "r")
        s = f.read()
        f.close()
        return s.split("\n")[item]



f1 = File("/home/dm/Documents/python_course/src/test1.txt")
f1.write('String for test1')
f2 = File("/home/dm/Documents/python_course/src/test2.txt")
f2.write('String for test2')
f3 = f1 + f2
print(f1)
print(f2)
print(f3)
print(f1.read())
print(f2.read())
print(f3.read())
# f1.write("String for test1")
for line in File('file.txt'):
    print(line)

print(os.path.exists(f3))