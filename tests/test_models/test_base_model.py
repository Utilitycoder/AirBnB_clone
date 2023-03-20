#!/usr/bin/python3
""" module for testing base model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class test_BaseModel(unittest.TestCase):

    """class for testing BaseModel"""
    def test_exist(self):

        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        var = BaseModel()
        self.assertEqual(str, type(var.id))
        a = BaseModel()
        b = BaseModel()
        a1 = a.id
        b1 = b.id
        self.assertNotEqual(a1, b1)

    def test_datetime(self):
        """this function test existence, difference and updates\
              of created_at and updated_at"""
        var = BaseModel()
        self.assertEqual(datetime, type(var.created_at))
        self.assertEqual(datetime, type(var.updated_at))
        var1 = BaseModel()
        sleep(0.1)
        var2 = BaseModel()
        self.assertLess(var1.created_at, var2.created_at)
        self.assertLess(var1.updated_at, var2.updated_at)
        a = var1.created_at
        b = var1.updated_at
        var1.id = "777"
        var1.save()
        self.assertEqual(a, var1.created_at)
        self.assertLess(b, var1.updated_at)

    def test_str_representation(self):

        var = BaseModel()
        var.id = "777"
        date = datetime.today()
        var.created_at = var.updated_at = str(date)
        var_str = var.__str__()
        self.assertIn("[BaseModel] (777)", var_str)
        self.assertIn("'id': '777'", var_str)
        self.assertIn(f"'created_at': '{str(date)}'", var_str)
        self.assertIn(f"'updated_at': '{str(date)}'", var_str)

    def test_args_as_None(self):

        """ passing args as None"""
        var = BaseModel(None)
        self.assertIn('created_at', var.__dict__.keys())
        self.assertIn('id', var.__dict__)
        self.assertNotIn(None, var.__dict__.values())

        """ passing kwargs as None """
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)
    
    def test_kwargs(self):
        dat = datetime.today()
        date = dat.isoformat()
        var = BaseModel("77",name="var", id="777", created_at=date, updated_at=date)
        self.assertEqual(var.id, "777")
        self.assertEqual(var.created_at, dat)
        self.assertEqual(var.updated_at, dat)
        self.assertEqual(var.name, "var")


    def test_save_method(self):

        var = BaseModel()
        first_uptdate = var.updated_at
        sleep(0.05)
        var.id = "777"
        var.save()
        self.assertLess(first_uptdate, var.updated_at)
        sec_update = var.updated_at
        sleep(0.05)
        var.save()
        self.assertLess(sec_update, var.updated_at)

    def test_to_dict(self):

        var = BaseModel()
        var.id = "777"
        var.name = "capital"
        date = datetime.today()
        var.created_at = var.updated_at = date
        todict = var.to_dict()
        self.assertEqual(dict, type(todict))
        self.assertIn('id', todict)
        self.assertIn('created_at', todict)
        self.assertIn('updated_at', todict)
        self.assertIn('__class__', todict)
        self.assertIn('name', todict)
        self.assertEqual(str, type(todict['created_at']))
        self.assertEqual(str, type(todict['id']))
        tdict = {
                '__class__': 'BaseModel',
                'id': '777',
                'name': 'capital',
                'created_at': date.isoformat(),
                'updated_at': date.isoformat()
                }
        self.assertDictEqual(tdict, todict)
        self.assertNotEqual(var.__dict__, todict)

    def test_save_reload_base_model(self):
        var = BaseModel()
        bm = "BaseModel." + var.id
        with open("file.json", "r") as f:
            self.assertNotIn(bm, f.read())
        var.save()
        with open("file.json", "r") as f:
            self.assertIn(bm, f.read())


if __name__ == "__main__":
    unittest.main()
