import unittest

#!/usr/bin/env python

"""
Tests for Liten2
"""

import unittest
import sqlite3
from time import strftime
import os
import liten2


class TestWalk(unittest.TestCase):

    def test_findthis(self):
        path = os.getcwd()
        size = 1048576
        walk = liten2.Walk(path, size)
        walk.findthis()
        expected = path+'/'+strftime('%Y-%m-%d.sql')
        result = os.path.isfile(expected)
        self.assertTrue(result)

class TestReport(unittest.TestCase):


    def test_db_connect(self):
        """Connectivity to the DB"""
        self.dump = strftime('%Y-%m-%d.sql')
        connection = True
        try:
            self.sqlfile = open(self.dump)
            self.conn = sqlite3.connect(':memory:', isolation_level='exclusive')
        except:
            connection = False
        self.assertTrue(connection)    

    def test_file_num(self):
        report = liten2.Report(full=False)
        for i in report.file_num():
            result = i[0]
        self.assertFalse(result)

#    def test_fullreport(self):
        # report = Report(full)
        # self.assertEqual(expected, report.fullreport())
#        assert False # TODO: implement your test here

#    def test_humanvalue(self):
        # report = Report(full)
        # self.assertEqual(expected, report.humanvalue(value))
#        assert False # TODO: implement your test here

#    def test_path_dups(self):
        # report = Report(full)
        # self.assertEqual(expected, report.path_dups())
#        assert False # TODO: implement your test here

#    def test_size_dups(self):
        # report = Report(full)
        # self.assertEqual(expected, report.size_dups())
#        assert False # TODO: implement your test here

#    def test_size_searched(self):
        # report = Report(full)
        # self.assertEqual(expected, report.size_searched())
#        assert False # TODO: implement your test here

#    def test_total_files(self):
        # report = Report(full)
        # self.assertEqual(expected, report.total_files())
#        assert False # TODO: implement your test here

#    def test_totalmb(self):
        # report = Report(full)
        # self.assertEqual(expected, report.totalmb())
#        assert False # TODO: implement your test here

#class TestDbWork(unittest.TestCase):
#    def test___init__(self):
        # db_work = DbWork()
#        assert False # TODO: implement your test here

#    def test_export(self):
        # db_work = DbWork()
        # self.assertEqual(expected, db_work.export())
#        assert False # TODO: implement your test here

#    def test_insert(self):
        # db_work = DbWork()
        # self.assertEqual(expected, db_work.insert(fileinfo, size, checksum))
#        assert False # TODO: implement your test here

#    def test_insert_opts(self):
        # db_work = DbWork()
        # self.assertEqual(expected, db_work.insert_opts(searched_files, size))
#        assert False # TODO: implement your test here

#class TestMain(unittest.TestCase):
#    def test_main(self):
        # self.assertEqual(expected, main())
#        assert False # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
