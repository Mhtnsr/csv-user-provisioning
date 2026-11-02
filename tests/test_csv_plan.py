import io
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from csv_plan import build_plan
HEADER='username,given_name,surname,department\n'
class CsvPlanTests(unittest.TestCase):
    def test_valid_and_normalized(self):
        plan=build_plan(io.StringIO(HEADER+'LAB.User01,Alex,Example,Lab\n'))
        self.assertEqual(plan['users'][0]['username'],'lab.user01')
        self.assertIs(plan['users'][0]['enabled'],False)
    def test_rejected_inputs(self):
        cases=['username,password\nu,secret\n',HEADER,HEADER+'bad;id,A,B,Lab\n',
               HEADER+'user,A,B,Lab\nUSER,A,B,Lab\n',HEADER+'user,=formula,B,Lab\n',
               HEADER+'user,A,B\n',HEADER+'user,A,B,Lab,extra\n',HEADER+'user,,B,Lab\n']
        for source in cases:
            with self.subTest(source=source):
                with self.assertRaises(ValueError): build_plan(io.StringIO(source))
if __name__=='__main__': unittest.main()
