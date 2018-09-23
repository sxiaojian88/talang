from talang.util.database.sqlite_client import SqliteClient
import sqlite3
import talang.util.util_data as ut
import talang.util.model.GreedMark as greed_mark_model
import talang.util.model.Position as position_model
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
    databaseManage = DatabaseManage()

    #1、创建greed_mark表
    greed_mark_get = greed_mark_model.GreedMark()
    databaseManage.create_table(greed_mark_get.tablename(), greed_mark_get.columns(), greed_mark_get.types(), greed_mark_get.primary_key_index())

    #2、查询greed_mark表
    #greed_marks = greed_mark_model.GreedMarks
    #greed_mark = greed_marks.select_greedmark_from_database()
    #greed_mark.print_detail()

    #3、创建position表
    #position = position_model.Position()
    #databaseManage.create_table(position.tablename(), position.columns(), position.types(), position.primary_key_index())
