import pymysql

class SQLink:
    db = 0
    db_host = '119.23.36.18'
    db_port = 3306
    db_name = 'test_market'
    db_user = 'test_market'
    db_passed = 'GrZFWfSh4GTMRBFy'
    def __init__(self):
        """初始化，返回连接id"""
        self.db = pymysql.connect(host = self.db_host, port = self.db_port, db = self.db_name, user = self.db_user, passwd = self.db_passed)

    def turn_off(self):
        """关闭连接"""
        self.db.close()

pdo = SQLink()

pdo.turn_off()