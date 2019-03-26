import mysql.connector


class MySQLDB:
    def __init__(self, host='', user='', password=input("Enter password for chosen database:\n"), database=''):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.connection = mysql.connector.connect(host=host, user=user, passwd=password, database=database)
        self.cursor = self.connection.cursor()

        self.cursor.execute("SHOW TABLES")
        self.list_tables = [t[0] for t in self.cursor]

    def __repr__(self):
        return "MySQL Database: {}\n" \
               "host: {}\n" \
               "user: {}\n" \
               "password: *******\n" \
               "Tables: {}".format(self.database, self.host, self.user, self.list_tables)

    def __str__(self):
        printout = ''
        for table in self.list_tables:
            printout += '\n\n{}\n'.format(table).upper()
            printout += '--\t{:40}\t-----'.format('-----')
            printout += '\nID\t{:40}\tSCORE\n'.format('TITLE')
            printout += '--\t{:40}\t-----'.format('-----')
            self.cursor.execute("SELECT * FROM {}".format(table))
            for row in self.cursor:
                printout += '\n{:}\t{:40}\t{}'.format(row[0], row[1], row[2])
        return printout


d = MySQLDB(host='localhost', user='root', database='evaluations')
print(repr(d))
print(d)