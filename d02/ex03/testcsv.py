from csvreader import CsvReader

if __name__ == "__main__":
    try:
        print('test')
        with CsvReader('good.csv') as file:
            print('test2vngh')
            if file == None:
                print("File is corrupted")
            #data = file.getdata()
            #header = file.getheader()
            file.close()
    except  ValueError as err:
        print(err)
