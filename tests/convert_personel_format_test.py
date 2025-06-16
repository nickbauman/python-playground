import unittest

from src.convert_personel_format import convert_personel_format

"""
Rename keys:
 - firstName+lastName → full-name,
 - emailAddress → email,
 - totalCount → count
 - Transform boolean isActive to string status ("active"/"inactive")
 Rename top-level users to user-lis
"""


def old_format_data():
    return {
        "users": [
            {
                "firstName": "John",
                "lastName": "Doe",
                "emailAddress": "john@example.com",
                "isActive": True,
            },
            {
                "firstName": "Jane",
                "lastName": "Smith",
                "emailAddress": "jane@example.com",
                "isActive": False,
            },
        ],
        "totalCount": 2,
    }


def new_format_data():
    return {
        "user-list": [
            {"full-name": "John Doe", "email": "john@example.com", "status": "active"},
            {
                "full-name": "Jane Smith",
                "email": "jane@example.com",
                "status": "inactive",
            },
        ],
        "count": 2,
    }


class ConvertPersonelFormatTest(unittest.TestCase):
    def test_convert_personel_format(self):
        result = convert_personel_format(old_format_data())
        self.assertEqual(result, new_format_data())
