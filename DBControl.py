import sqlite3


class DBControl:

    @staticmethod
    def import_data(data_transform):
        # TODO: Add in error catching. What if scan results is empty??

        # Create & Connect to Database
        data_base_file_name = 'Network_Scan_Database.db'
        conn = sqlite3.connect('Network_Scan_Database.db')
        c = conn.cursor()

        # Create Table
        c.execute("DROP TABLE IF EXISTS DB") #Delete Old Data

        c.execute('''CREATE TABLE IF NOT EXISTS DB
                     (IP_Adress text, Host_Name text)''')

        # Populate Table
        # TODO: Other data needs to be added to table: hostname, IP, ports, etc.
        for i in range(len(data_transform.ip_addresses)):
            command = "INSERT INTO DB VALUES ('" + data_transform.ip_addresses[i] + "','" + data_transform.host_name[i] + "')"
            c.execute(command)
            conn.commit()

        # Close Database
        conn.close()
        return data_base_file_name



