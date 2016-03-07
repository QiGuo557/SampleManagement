import sqlite3


def insert_sample(new_sample):
    """ Insert samples to database
    :param new_sample: Samples received from frontend
    """
    conn = sqlite3.connect('sample.db')
    conn.execute("""INSERT INTO sample (Name,Chemical,Notes) VALUES (?, ?, ?)""", (new_sample.name,
                                                                                   new_sample.chemical,
                                                                                   new_sample.notes))
    conn.commit()
    conn.close()


def edit_sample(sample):
    """ Edit samples in the database
    :param sample: Samples received from frontend
    """
    conn = sqlite3.connect('sample.db')
    conn.execute("""UPDATE Sample SET Name= ?, Chemical = ?, Notes = ? WHERE ID=?""",
                 (sample.name, sample.chemical, sample.notes, sample.id))
    conn.commit()
    conn.close()


def search_all_sample():
    """ Select all the samples from database
    :return samples: A list that contains all the samples from database
    """
    conn = sqlite3.connect('sample.db')
    sample_list = conn.execute("SELECT * FROM Sample")
    samples = []
    for item in sample_list:
        sample = {'id': item[0], 'name': item[1], 'chemical': item[2], 'notes': item[3]}
        samples.append(sample)
    conn.close()
    return samples
