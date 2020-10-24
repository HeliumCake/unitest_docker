import unittest
from .post import post_params_check


class PostCheckTest(unittest.TestCase):
    def test_example(self):
        # 标题缺失
        content = {
            'content': '123456789012345'
        }
        self.assertEqual(post_params_check(content), ("title", False))

    def test_example_2(self):
        # 标题不是字符串
        content = {
            'title': 1,
            'content': '123456789012345'
        }
        self.assertEqual(post_params_check(content), ("title", False))

    def test_example_3(self):
        # 标题长度小于1
        content = {
            'title': '',
            'content': '123456789012345'
        }
        self.assertEqual(post_params_check(content), ("title", False))

    def test_example_4(self):
        # 标题长度大于64
        content = {
            'title': '12345678901234567890'
                     '12345678901234567890'
                     '1234567890123456789012345',
            'content': '123456789012345'
        }
        self.assertEqual(post_params_check(content), ("title", False))

    def test_example_5(self):
        # 帖子内容缺失
        content = {
            'title': '12345'
        }
        self.assertEqual(post_params_check(content), ("content", False))

    def test_example_6(self):
        # 帖子内容不是字符串
        content = {
            'title': '12345',
            'content': 12345
        }
        self.assertEqual(post_params_check(content), ("content", False))

    def test_example_7(self):
        # 帖子内容长度小于15
        content = {
            'title': '12345',
            'content': '12345'
        }
        self.assertEqual(post_params_check(content), ("content", False))

    def test_example_8(self):
        # 帖子内容长度大于256
        content = {
            'title': '12345',
            'content': '1234567890123456789012345678901234567890'
                       '1234567890123456789012345678901234567890'
                       '1234567890123456789012345678901234567890'
                       '1234567890123456789012345678901234567890'
                       '1234567890123456789012345678901234567890'
                       '1234567890123456789012345678901234567890'
                       '12345678901234567'
        }
        self.assertEqual(post_params_check(content), ("content", False))

    def test_example_9(self):
        # 正常帖子
        content = {
            'title': '12345',
            'content': '123456789012345'
        }
        self.assertEqual(post_params_check(content), ("ok", True))

    def test_example_10(self):
        # 标题内容均缺失
        content = {}
        self.assertEqual(post_params_check(content), ("title", False))

    def test_example_11(self):
        # 标题内容均不是字符串
        content = {
            'title': 12345,
            'content': 12345
        }
        self.assertEqual(post_params_check(content), ("title", False))

    def test_example_12(self):
        # 标题内容长度均不正确
        content = {
            'title': '',
            'content': '12345'
        }
        self.assertEqual(post_params_check(content), ("title", False))

    def test_example_13(self):
        # 标题内容均缺失
        self.assertEqual(post_params_check(None), ("title", False))


if __name__ == '__main__':
    unittest.main()
