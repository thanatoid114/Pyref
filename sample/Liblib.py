import sqlite3
import os
import Biblib as bib


class library(object):
    # Define the parameters to local *.db file
    _library_list = ('db_file', 'db_file_path')

    def __init__(self):
        # generate a libaray object
        self.lib_content = {item: '' for item in self._library_list}

    def connect_2db(self, file_path=''):
        # connect the the datebase file retrun the cursor object
        db_lib_cursor = sqlite3.connect(file_path)
        self.lib_content['db_file'] =\
            os.path.splitext(os.path.basename(file_path))[0]
        self.lib_content['db_file_path'] = file_path
        return db_lib_cursor

    def add_2_lib(self, bib_obj=bib.bibitem()):
        # add a bibitem to the db file
        status = 1
        return status
