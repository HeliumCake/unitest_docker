import unittest
from .post import post_params_check


class PostCheckTest(unittest.TestCase):
    def test_example(self):
        # 标题缺失
        self.assertEqual(post_params_check(content="123456789012345"), ("title", False))

    def test_example_2(self):
        # 标题不是字符串
        self.assertEqual(post_params_check(1, "123456789012345"), ("title", False))

    def test_example_3(self):
        # 标题长度小于1
        self.assertEqual(post_params_check("", "123456789012345"), ("title", False))

    def test_example_4(self):
        # 标题长度大于64
        self.assertEqual(post_params_check("12345678901234567890"
                                           "12345678901234567890"
                                           "1234567890123456789012345", "123456789012345"), ("title", False))

    def test_example_5(self):
        # 帖子内容缺失
        self.assertEqual(post_params_check(title="12345"), ("content", False))

    def test_example_6(self):
        # 帖子内容不是字符串
        self.assertEqual(post_params_check("12345", 12345), ("content", False))

    def test_example_7(self):
        # 帖子内容长度小于15
        self.assertEqual(post_params_check("12345", "12345"), ("content", False))

    def test_example_8(self):
        # 帖子内容长度大于256
        self.assertEqual(post_params_check("12345", "1234567890123456789012345678901234567890"
                                                    "1234567890123456789012345678901234567890"
                                                    "1234567890123456789012345678901234567890"
                                                    "1234567890123456789012345678901234567890"
                                                    "1234567890123456789012345678901234567890"
                                                    "1234567890123456789012345678901234567890"
                                                    "12345678901234567"), ("content", False))

    def test_example_9(self):
        # 正常帖子
        self.assertEqual(post_params_check("12345", "123456789012345"), ("ok", True))

    def test_example_10(self):
        # 标题内容均缺失
        self.assertEqual(post_params_check(), ("title", False))

    def test_example_11(self):
        # 标题内容均不是字符串
        self.assertEqual(post_params_check(12345, 12345), ("title", False))

    def test_example_12(self):
        # 标题内容长度均不正确
        self.assertEqual(post_params_check("", "12345"), ("title", False))


if __name__ == '__main__':
    unittest.main()
