from unittest.mock import MagicMock

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
    def test_global_vars(self):
        M = MemoKid
        self.pump_events()
        self.assertEqual(M.answer_dict,{},"Answer_dict not empty")
        self.assertEqual(M.answer_list, [],"Ansswer_list not empty")
        self.assertEqual(M.count, 0, "count not zero")
        self.assertEqual(M.clicks, 0, "clicks not zero")
        self.assertEqual(M.succesess, 0,"successes not zero")
        self.pump_events()

    def test_LevelClass(self):
        M = MemoKid
        self.pump_events()
        with self.assertRaises(TypeError):
            M.LevelClass(111)
        try:
            M.LevelClass(315848820)
        except TypeError:
            self.fail("TypeError LevelClass with valid user")


    def test_LevelClassA_CalledAndNotCalled(self):
        M = MemoKid
        self.pump_events()
        with patch.object(M, 'Level1A') as mock:
            M.LevelClass(123456789)
            self.pump_events()
        mock.assert_called_once_with(123456789)
        self.pump_events()
        with patch.object(M, 'Level1A') as mock2:
            M.LevelClass(316432137)
            self.pump_events()
        mock2.assert_not_called()

    def test_LevelClassB_CalledAndNotCalled(self):
        M = MemoKid
        self.pump_events()
        with patch.object(M, 'Level1B') as mock:
            M.LevelClass(316432137)
            self.pump_events()
        mock.assert_called_once_with(316432137)
        self.pump_events()
        with patch.object(M, 'Level1B') as mock2:
            M.LevelClass(555)
            self.pump_events()
        mock2.assert_not_called()

    def test_LevelClassC_CalledAndNotCalled(self):
        M = MemoKid
        self.pump_events()
        with patch.object(M, 'Level1C') as mock:
            M.LevelClass(555)
            self.pump_events()
        mock.assert_called_once_with(555)
        self.pump_events()
        with patch.object(M, 'Level1C') as mock2:
            M.LevelClass(316432137)
            self.pump_events()
        mock2.assert_not_called()

    def test_CheckUserType(self):
        M = MemoKid
        self.pump_events()
        with self.assertRaises(TypeError):
            M.CheckUserType(111)
        try:
            M.CheckUserType(315848820)
        except TypeError:
            self.fail("TypeError with valid user")

    def test_CheckUserType_Student_CalledAndNotCalled(self):
        M = MemoKid
        self.pump_events()
        with patch.object(M, 'MenuPageStudent') as mock:
            M.CheckUserType(316432137)
            self.pump_events()
        mock.assert_called_once_with(316432137)
        self.pump_events()
        with patch.object(M, 'MenuPageStudent') as mock2:
            M.CheckUserType(315848820)
            self.pump_events()
        mock2.assert_not_called()
        self.pump_events()

    def test_CheckUserType_Admin_CalledAndNotCalled(self):
        M = MemoKid
        self.pump_events()
        with patch.object(M, 'MenuPageAdmin') as mock:
            M.CheckUserType(315848820)
            self.pump_events()
        mock.assert_called_once()
        self.pump_events()
        with patch.object(M, 'MenuPageAdmin') as mock2:
            M.CheckUserType(316432137)
            self.pump_events()
        mock2.assert_not_called()
        self.pump_events()

    def test_CheckUserType_Research_CalledAndNotCalled(self):
        M = MemoKid
        self.pump_events()
        with patch.object(M, 'MenuPageResearch') as mock:
            M.CheckUserType(1020304050)
            self.pump_events()
        mock.assert_called_once()
        self.pump_events()
        with patch.object(M, 'MenuPageResearch') as mock2:
            M.CheckUserType(316432137)
            self.pump_events()
        mock2.assert_not_called()
        self.pump_events()

    def test_ShowLastGames_User(self):
        M = MemoKid
        self.pump_events()
        with self.assertRaises(TypeError):
            M.ShowLastGames(111)
        try:
            M.ShowLastGames(315848820)
        except TypeError:
            self.fail("TypeError with valid user")

    def test_SearchInList(self):
        M = MemoKid
        self.pump_events()
        tmplist = (15,27,50)
        self.assertTrue(M.SearchInList(tmplist, 15))
        self.assertFalse(M.SearchInList(tmplist, 28))

    def test_GetDifficultyFromClass(self):
        M = MemoKid
        self.pump_events()
        self.assertEqual(M.GetDifficultyFromClass('א'), 1)
        self.assertNotEqual(M.GetDifficultyFromClass('א'), 2)
        self.assertEqual(M.GetDifficultyFromClass('ב'), 1)
        self.assertNotEqual(M.GetDifficultyFromClass('ב'), 3)
        self.assertEqual(M.GetDifficultyFromClass('ג'), 2)
        self.assertNotEqual(M.GetDifficultyFromClass('ג'), 1)
        self.assertEqual(M.GetDifficultyFromClass('ד'), 2)
        self.assertNotEqual(M.GetDifficultyFromClass('ד'), 3)
        self.assertEqual(M.GetDifficultyFromClass('ה'), 3)
        self.assertNotEqual(M.GetDifficultyFromClass('ה'), 2)
        self.assertEqual(M.GetDifficultyFromClass('ו'), 3)
        self.assertNotEqual(M.GetDifficultyFromClass('ו'), 1)


    def test_GetDifficultyLevel2(self):
        M = MemoKid
        self.pump_events()
        self.assertEqual(M.GetDifficultyLevel2(1), 5)
        self.assertNotEqual(M.GetDifficultyLevel2(1), 7)
        self.assertEqual(M.GetDifficultyLevel2(2), 7)
        self.assertNotEqual(M.GetDifficultyLevel2(2), 5)
        self.assertEqual(M.GetDifficultyLevel2(3), 10)
        self.assertNotEqual(M.GetDifficultyLevel2(3), 7)

    def test_GetDifficultyLevel3(self):
        M = MemoKid
        self.pump_events()
        self.assertEqual(M.GetDifficultyLevel3(1), 4)
        self.assertNotEqual(M.GetDifficultyLevel3(1), 6)
        self.assertEqual(M.GetDifficultyLevel3(2), 6)
        self.assertNotEqual(M.GetDifficultyLevel3(2), 4)
        self.assertEqual(M.GetDifficultyLevel3(3), 8)
        self.assertNotEqual(M.GetDifficultyLevel3(3), 6)


if __name__ == '__main__':
    import unittest
    unittest.main()