class ReadFile(object):
    def __init__(self,filepath):
        self.filepath = filepath
    def read_file(self,):
        with open(self.filepath,'rb') as f:
            file_byte = f.read()
            return file_byte
    def file_length(self):
        length = len(self.read_file())
        return length
if __name__ == '__main__':
    readfile = ReadFile('../html/index.html')
    print(readfile.read_file())
    print(readfile.file_length())
