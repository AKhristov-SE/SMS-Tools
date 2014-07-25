import sqlite3
from core import Text


class IOS6:
    """ iOS 6 sqlite reader and writer """


    def parse(self, file):
        """ Parse iOS 6 sqlite file to Text[] """

        conn = sqlite3.connect(file)
        c = conn.cursor()
        i=0
        texts = []
        query = c.execute(
            'SELECT handle.id, message.date, message.is_from_me, message.text, message.handle_id \
             FROM message \
             INNER JOIN handle ON message.handle_id = handle.ROWID \
             ORDER BY message.ROWID ASC;')
        for row in query:
            if sms_debug and i > 80:
                return
            i+=1
            txt = Text(row[0],long((row[1] + 978307200)*1000),(row[2]==1),row[3])
            texts.append(txt)
            if sms_debug:
                print txt
        return texts

    def write(self, texts, outfile):
        raise Exception("not implemented!")
        #TODO !!!