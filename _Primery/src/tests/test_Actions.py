from unittest import TestCase

from tests.Actions import Actions
from tests.User import User


class TestActions(TestCase):
    def setUp(self): #метод запускается первым
        self.my_obj = Actions()
        self.user = User('Иван',20)

    # def tearDown(self) -> None: #данный метод запускается последним
    #
    def test_add_user(self):
        self.my_obj.add_user(self.user)
        self.assertEqual(len(self.my_obj.users),1)

    def test_remove_user(self):
        self.my_obj.remove_user(self.user)
        self.assertEqual(len(self.my_obj.users), 0)
