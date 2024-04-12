import sys

sys.path.append(
    "c:\\Users\\donut\\programming\\python_projects\\stabwerkmodelle\\src\\stabwerkmodelle"
)
import unittest
import mats_beton

x = mats_beton.f_cd(0.85, 30, 1.5)
y = mats_beton.hello()


class TestMatsBeton(unittest.TestCase):
    def test_f_cd(self):
        self.assertEqual(mats_beton.f_cd(0.85, 30, 1.5), 17.0)

    def test_hello(self):
        self.assertEqual(mats_beton.hello(), "Hello from .py")
        
if __name__ == '__main__':
    unittest.main()