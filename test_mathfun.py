import unittest
from mathfun import *

class TestMathFun(unittest.TestCase): #继承TestCase类
    @classmethod
    def setUpClass(cls):   #在所有case前执行一次
        print("这个setUpclass方法只执行一次\n")
    @classmethod    #在所有case后清理一次
    def tearDownClass(cls):
        print("这个tearDownclass方法也执行一次")
    def setUp(self):  #在每个测试方法执行前执行一次，用来为测试准备环境
        print("每个方法执行前执行一次，测试的准备环境")
    def tearDown(self):  #在每个测试方法执行后执行一次，用来为测试清理环境，以备之后的测试
        print("测试的清理环境\n")
    def test_add(self):
        print("Add")
        self.assertEqual(5,add(2,3))
        self.assertNotEqual(3,add(3,2))

    def test_minus(self):
        print("Minus")
        self.assertEqual(5,minus(6,1))
        self.assertNotEqual(1,minus(6,2))

    def test_multi(self):
        print("Multi")
        self.assertEqual(9,multi(3,3))
        self.assertNotEqual(4,multi(2,5))
    
    
    #skip装饰器有三个：1.unittest.skip(reason),无条件跳过；
    # 2.unittest.skipIf(condition,reason),当condition为True时跳过；
    # 3.unittest.skipUnless(condition,reason),当condition为Flase时跳过；   
    
    # @unittest.skip("我不想执行这个case") skip装饰器跳过某个case   
    def test_divide(self):
        # self.skipTest("不执行") #用.skipTest()方法将跳过test_divide这个case的执行
        print("Divide")
        self.assertEqual(3,divide(9,3))
        self.assertNotEqual(6,divide(12,2))
if __name__ == "__main__":
    unittest.main()