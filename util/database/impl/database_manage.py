from talang.util.database.sqlite_client import SqliteClient
import sqlite3
import talang.util.util_data as ut
import talang.util.model.GreedMark as greed_mark_model
import pickle as pickle


class DatabaseManage:

    def __init__(self):
        """
        Constructor
        """
        self.db_client = SqliteClient()
        self.db_client.connect(path=ut.SQLPLITE_PATH)
        self.is_database_defined = True

        pass

    def create_table(self, table_name, columns, types, primary_key_index=[], is_ifnotexists=True):
        self.db_client.create(table_name, columns, types, primary_key_index, is_ifnotexists)

        return True

if __name__ == "__main__":
    greed_mark_get = greed_mark_model.GreedMark()

    databaseManage = DatabaseManage()
    #databaseManage.create_table(greed_mark.tablename(), greed_mark.columns(), greed_mark.types(), greed_mark.primary_key_index())

    greed_marks = greed_mark_model.GreedMarks
    greed_mark = greed_marks.select_greedmark_from_database()
    greed_mark.print_detail()