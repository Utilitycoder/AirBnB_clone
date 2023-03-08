#!/usr/bin/python3
""" module for testing base model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class test_BaseModel(unittest.TestCase):

    """class for testing BaseModel"""
    def test_exist(self):

        self.assertEqual(BaseModel, BaseModel())

    def test_id(self):

        self.assertEqual(str, type(BaseModel.id))
        a = BaseModel.id
        b = BaseModel.id
        self.assertNotEqual(a, b)

    def test_datetime(self):
        """this function test existence, difference and updates\
              of created_at and updated_at"""
        self.assertEqual(datetime, type(BaseModel.created_at))
        self.assertEqual(datetime, type(BaseModel.updated_at))
        var1 = BaseModel()
        sleep(0.1)
        var2 = BaseModel()
        self.assertLess(var1.created_at, var2.created_at)
        self.assertLess(var1.updated_at, var2.update_at)
        a = var1.created_at
        b = var1.update_at
        var1.id = "777"
        self.assertEqual(a, var1.created_at)
        self.assertLess(b, var1.update_at)

    def test_str_representation(self):

        var = BaseModel()
        var.id = "777"
        date = datetime.today()
        var.created_at = var.updated_at = str(date)
        var_str = var.__str__()
        self.assertIn("[BaseModel] (777)", var_str)
        self.assertIn("'id': 777")
        self.assertIn("'created_at': " + str(date), var_str)
        self.assertIn("'updated_at': " + str(date), var_str)

    def test_save_method(self):

        var = BaseModel()
        first_uptdate = var.updated_at
        sleep(0.05)
        var.id = "777"
        var.save()
        self.assertLess(first_uptdate, var.update_at)
        sec_update = var.update_at
        sleep(0.05)
        var.save()
        self.assertLess(sec_update, var.update_at)

    def test_to_dict(self):

        var = BaseModel()
        var.id = "777"
        var.name = "capital"
        date = datetime.today()
        var.created_at = var.updated_at = str(date)
        todict = var.to_dict()
        self.assertEqual(dict, type(todict))
        self.assertIn("'id': 777")
        self.assertIn("'created_at'", todict)
        self.assertIn("'updated_at'", todict)
        self.assertIn("'__class__'", todict)
        self.assertIn("'name'", todict)
        self.assertEqual(str, type(todict['created_at']))
        self.assertEqual(str, type(todict['id']))
        tdict = {
                '__class__': 'BaseModel',
                'id': '777',
                'created_at': date.isoformat,
                'updated_at': date.isoformat
                }
        self.assertDictEqual(tdict, todict)
        self.assertNotEqual(var.__dict__, todict)


if __name__ == "__main__":
    unittest.main()
