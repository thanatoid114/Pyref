from context import Biblib as bib
from context import Liblib as lib

a = bib.bibitem()
a.get_bib_item_from_file('test.bibtex')
# print(a.bib_content)
# a.edit_bib()
b = lib.library()
b.connect_2db('test.db')
b.add_2_lib(a)
b.close_2db()
