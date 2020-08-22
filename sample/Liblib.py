import sqlite3
from sqlite3 import Error
import os
import Biblib as bib

# Oranage the sqlite operation


class library(object):
    # Define the parameters to local *.db file
    _library_list = ('db_file', 'db_file_path')

    def __init__(self):
        # generate a libaray object
        self.lib_content = {item: '' for item in self._library_list}
        bibtemp = bib.bibitem()
        self.lib_table = [item for item in bibtemp._content_list]
        self.db_lib_cursor = None

    def connect_2db(self, file_path=''):
        # connect the the datebase file retrun the cursor object or if
        # it is not exit create it
        try:
            self.db_lib_cursor = sqlite3.connect(file_path)
            print(sqlite3.version)
            self.lib_content['db_file'] =\
                os.path.splitext(os.path.basename(file_path))[0]
            self.lib_content['db_file_path'] = file_path
        except Error as e:
            print(e)
        finally:
            self.db_lib_cursor.execute("""
            CREATE TABLE IF NOT EXISTS lib_table(
            cite_key TEXT NOT NULL UNIQUE,
            type TEXT DEFAULT NULL,
            author TEXT DEFAULT NULL,
            title TEXT DEFAULT NULL,
            journal TEXT DEFAULT NULL,
            year TEXT DEFAULT NULL,
            keywords TEXT DEFAULT NULL,
            url TEXT DEFAULT NULL,
            doi TEXT DEFAULT NULL,
            file_path TEXT DEFAULT NULL,
            full_content TEXT DEFAULT NULL);
            """)

    def close_2db(self):
        # save and close the connection to the date base
        self.db_lib_cursor.close()

    def add_2_lib(self, bib_obj=bib.bibitem()):
        # add a bibitem to the db file
        sql_add = """INSERT INTO lib_table(cite_key,type,author,title,journal,year,keywords,url,doi,file_path,full_content) VALUES (?,?,?,?,?,?,?,?,?,?,?);"""
        arg_list = [bib_obj.bib_content[item] for item in self.lib_table]
        arg_tuple = tuple(arg_list)
        try:
            self.db_lib_cursor.execute(sql_add, arg_tuple)
            self.db_lib_cursor.commit()
        except Error as e:
            print(e)

    # def update_citekey(self):
        # update the citation key for the select one
