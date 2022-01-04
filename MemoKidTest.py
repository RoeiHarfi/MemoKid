import MemoKid
import unittest
import tkinter
import _tkinter
import mock
from mock import patch



class TKinterTestCase(unittest.TestCase):
    def setUp(self):
        self.root=tkinter.Tk()
        self.pump_events()

    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.pump_events()

    def pump_events(self):
        while self.root.dooneevent(_tkinter.ALL_EVENTS | _tkinter.DONT_WAIT):
            pass

class TestMemoKid(TKinterTestCase):
    def test_answerdict(self):
        M = MemoKid
        self.pump_events()
        self.assertEqual(M.answer_dict,{},"TEST ANSWER DICT NOT OK")
        self.pump_events()

    def test_LevelClass(self):
        M = MemoKid
        self.pump_events()
        with patch.object(M, 'Level1C') as mock:
            M.LevelClass(555)
            self.pump_events()
        mock.assert_called_once_with(555)
        self.pump_events()

    def test_login_student(self):
        M = MemoKid
        self.pump_events()
        with patch.object(M, 'MenuPageStudent') as mock:
            M.LoginPage.



if __name__ == '__main__':
    import unittest
    unittest.main()