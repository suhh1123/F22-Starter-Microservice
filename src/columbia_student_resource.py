import pymysql

import os


class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = "admin"
        pw = "suhaohua520"
        h = "comse6156-hw0-instance.cpes1g4l3sdp.us-east-2.rds.amazonaws.com"

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM comse6156_hw0_db.columbia_student where uni=%s";
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

