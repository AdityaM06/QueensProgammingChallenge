import os, time

class Database:

    """ Constructor """
    def __init__(self):
        # Name of file with database info
        self.FILEPATH = "database.file"
        
        # Get relevant directories for reading files
        self.DIR = str ( os.path.dirname(os.path.realpath(__file__)) )
        self.FILE_DIR = self.DIR + "\\" + self.FILEPATH

        # Organizing data   [PASS, INFO, INFO, INFO, INFO]
        self.data_indexes = [ 0,    1,    2,    3,    4  ]

        # Read file into RAM as dictionary
        self._data = self.read_file(self.FILE_DIR)

    """ Reads the file upon start to load all data """
    def read_file(self, filepath):
        # Var to be returned
        final_dict = {}

        # Read file
        with open(filepath, "r+") as f:
            # First lines are comments, skip
            f.readline(); f.readline()

            # Loop through each line
            while True:
                # Read line, quit if its empty
                line = f.readline()
                if not line: break
                
                # Format data and add to dict
                line = line.split(',')
                key = line[0]; del line[0]
                final_dict[key] = line

        # print(final_dict)
        return final_dict


    """ Returns True if the key exists in the database """
    def keyExists(self, key : str) -> bool:
        return key in self._data

    def addKey(self, key : str, data):
        print(f"[DATABASE] Adding new data: ({key}, {data})")

        # Write data locally
        self._data[key] = data

        # Write data to file
        with open(self.FILE_DIR, 'a+') as f:
            f.write(key)

            for d in data: f.write(f",{d}")
            f.write("\n")



    """ Returns the PassHash of the User """
    def getPassHash(self, key : str):
        if ( not key in self._data): raise ValueError("Key Does not Exist in Database")
        return self._data[key][ self.data_indexes[0] ]

    """ TODO REMAIN TO BE DEFINED """
    def info1(self, key : str):
        if ( not key in self._data): raise ValueError("Key Does not Exist in Database")
        return self._data[key][ self.data_indexes[1] ]
    def info2(self, key : str):
        if ( not key in self._data): raise ValueError("Key Does not Exist in Database")
        return self._data[key][ self.data_indexes[2] ]
    def info3(self, key : str):
        if ( not key in self._data): raise ValueError("Key Does not Exist in Database")
        return self._data[key][ self.data_indexes[3] ]
    def info4(self, key : str):
        if ( not key in self._data): raise ValueError("Key Does not Exist in Database")
        return self._data[key][ self.data_indexes[4] ]
    
    
                
""" Dump database contents, used for debugging """
def dump():
    db = Database()
    print(db._data)

# dump()