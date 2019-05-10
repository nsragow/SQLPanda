
import pandas as pd, sqlite3

class Sqldf:
    '''
    Wraps SQLite3 instance to streamline the SQL query to Pandas DataFrame process.

    Ex./

        import SQL_Panda as spd

        sdf = spd.Sqldf("data.sqlite")
        #where data.splite is the SQLite DB file

    Main method examples:
        sdf.q("Select * from table_name")

        sdf.tables()

        sdf.head("table_name")
    '''
    def __init__(self,path):
        '''
        Ex./
            sdataframe = Sqldf("data.sqlite")
        '''
        self.conn = sqlite3.connect(path)
        self.c = self.conn.cursor()
    def q(self,query):
        '''
        For general soft queries. Does not mutate database file, but will add changes to cursor.

        Parameters:
            query:
                SQL query as string
        Returns:
            Panda dataframe (empty if no respose).
        '''
        self.c.execute(query)
        fetched = self.c.fetchall()
        columns = [x[0] for x in self.c.description]
        if len(fetched) == 0:
            return pd.DataFrame(columns=columns)
        df = pd.DataFrame(fetched)
        df.columns = columns
        return df
    def tables(self):
        '''
        Returns:
            Panda series with all table names in DB.
        '''
        return self.q('Select name from sqlite_master where sqlite_master.type like \'table\'')
    def info(self):
        '''
        Returns:
            Pandas dataframe with all info from sqlite_master
        '''
        return self.q('Select * from sqlite_master')
    def head(self,table,length = 5):
        '''
        Similar to Pandas head method, but requires a table name.

        Parameters:
            table:
                table name as string
            length:
                count of rows to return
        Returns:
            Pandas dataframe of head of table
        '''
        return self.q(f'Select * from {table} limit {length}')
    def commit(self,query):
        '''
        Runs query and writes back all changes to database file.

        see Sqldf.q() for details
        '''
        df = self.q(query)
        self.conn.commit()
        return df