class Sample(object):
    """Sample class with id, name, chemical, notes"""
    id = -1
    name = ''
    chemical = ''
    notes = ''

    def __init__(self, name, chemical, notes='', id=-1):
        """
        Construct a sample object
        :param name: sample name
        :param chemical: sample chemical
        :param notes: sample notes
        :param id: sample id (auto-incremented, initialized to be -1)
        :return: a sample object
        """
        self.id = id
        self.name = name
        self.chemical = chemical
        self.notes = notes


