from os import path


# WIP
class CsvReader:
    def __init__(self, file_name, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.file_name =  file_name
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
    
    def gethearder(self):
        header = self.file.readline()
        print(header)
    def  __enter__(self):
        print('__enter__')
        if path.isfile(self.file_name):
            print('__en2__')
            self.file = open(self.file_name, 'w')
            return self.file
        else:
            print('no a file')
            raise ValueError( self.file_name + 'do not exist or is not a valid  file ')
    
        #if header

    def __exit__(self,exception_type, exception_value, traceback):
        self.file.close() 

