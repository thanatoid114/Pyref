import re
import readline


class bibitem(object):
    """Define the list of contents will store in the bib object in the date base;
    Include the items for search in the data base and full original
    content and the access path to out side resource.
    """
    _content_list = ('type', 'cite_key',  # Important information for citation
                     'author', 'title', 'journal',
                     'year', 'keywords',  # For search
                     'url', 'doi', 'file_path',  # For access
                     'full_content')  # For all the other

    """
    # # Define the item content will tranfer to the library file; base on the
    # # standard bibtex format
    _bibtex_type_dict = {'article': ('cite-key', 'author',
                                     'title', 'journal', 'year',
                                     'volume', 'number', 'pages',
                                     'month', 'url', 'doi',),
                         'book': ('cite-key', 'title', 'publisher',
                                  'year', 'author', 'edition', 'volume',
                                  'number', 'series', 'address', 'edition',
                                  'url', 'doi',)
                         # Some other type may add ..
                         }
    # Define the bibtem
    We define several items separartly store in the bibtem and an
    independent item contain the full
    """

    def __init__(self):
        # generate a empty bibtex object
        self.bib_content = {item: '' for item in self._content_list}

    def _get_bib_file(self, path_str=''):
        # read a bib file
        try:
            with open(path_str, 'r', encoding='utf-8') as bib_text:
                bib_item = bib_text.read()
                return bib_item
        except OSError as err:
            print('can not load bibtex file, nothing is generated')
            print('OS error: {0}'.format(err))

    def _get_content(self, target_text='', item_text=''):
        """ Get the specific item information of bibtex file"""
        target_result = ''
        type_obj = re.search(r'(\s*'+target_text+'\s*=\s*{)(.*)(}[,\s]*)'
                             , item_text)
        if type_obj:
            target_result = str(type_obj.group(2))
        else:
            print(target_text + ' not found, empty by default')
        return target_result

    def _get_itype(self, item_text=''):
        """ Get the type of bibtex item."""
        itype = ''
        type_obj = re.search(r'(^@)([a-z]*)({)', item_text)
        if type_obj:
            itype = str(type_obj.group(2))
        else:
            print('item type not found')
        return itype

    def _get_icikey(self, item_text=''):
        """ Get the icikey of bibtex item."""
        icikey = ''
        type_obj = re.search(r'(^@)([a-z]*{)([^,]*),', item_text)
        if type_obj:
            icikey = str(type_obj.group(3))
        else:
            print('item cikey not found')
        return icikey

    def _gen_bib_item(self, bib_text):
        """ Generate the required bib item
        """
        bib_type = self._get_itype(bib_text)
        self.bib_content['type'] = bib_type
        self.bib_content['cite-key'] = self._get_icikey(bib_text)
        for bib_key in self._content_list[2:-3]:
            # bibtex type cite-key and the total contents
            # are need to get separately also for total keywords and file_path
            self.bib_content[bib_key] = self._get_content(
                    bib_key, bib_text)
            self.bib_content['full_content'] = bib_text

    def get_bib_item_from_file(self, path_str=''):
        """ Get a bib object based on a bibtex file from the input
        """
        bib_text = self._get_bib_file(path_str)
        self._gen_bib_item(bib_text)

        def gen_bib_item_4_db(self):
            """ Generate the item for the date base
        """
        for bib_key in self._content_list:
            print(bib_key+":"+self.bib_content[bib_key])

    def edit_bib(self):
        """ Change the content of the bibtex.
        readline or use some other application
        """
        readline.set_startup_hook(lambda: readline.insert_text(
            self.bib_content['full_content']))
        try:
            new_item = input("Edit:")
        finally:
            readline.set_startup_hook()
        self._gen_bib_item(new_item)

