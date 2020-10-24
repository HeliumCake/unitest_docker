import unittest
from .reply import reply_post_params_check


class ReplyCheckTest(unittest.TestCase):
    def test_example(self):
        # 回复id缺失
        self.assertEqual(reply_post_params_check(content="123456789012345"), ("ok", True))

    def test_example_2(self):
        # 回复id不是整数
        self.assertEqual(reply_post_params_check("123456789012345", "1"), ("replyId", False))

    def test_example_3(self):
        # 回复id不是非负
        self.assertEqual(reply_post_params_check("123456789012345", -1), ("replyId", False))

    def test_example_4(self):
        # 回复内容缺失
        self.assertEqual(reply_post_params_check(replyId=1), ("content", False))

    def test_example_5(self):
        # 回复内容不是字符串
        self.assertEqual(reply_post_params_check(12345, 1), ("content", False))

    def test_example_6(self):
        # 回复内容长度小于15
        self.assertEqual(reply_post_params_check("12345", 1), ("content", False))

    def test_example_7(self):
        # 回复内容长度大于256
        self.assertEqual(reply_post_params_check("1234567890123456789012345678901234567890"
                                                 "1234567890123456789012345678901234567890"
                                                 "1234567890123456789012345678901234567890"
                                                 "1234567890123456789012345678901234567890"
                                                 "1234567890123456789012345678901234567890"
                                                 "1234567890123456789012345678901234567890"
                                                 "12345678901234567", 1), ("content", False))

    def test_example_8(self):
        # 正常帖子
        self.assertEqual(reply_post_params_check("123456789012345", 1), ("ok", True))

    def test_example_9(self):
        # 回复内容和回复id均缺失
        self.assertEqual(reply_post_params_check(), ("content", False))

    def test_example_10(self):
        # 回复内容不是字符串，回复id不是整数
        self.assertEqual(reply_post_params_check(12345, "1"), ("content", False))

    def test_example_11(self):
        # 回复内容长度不正确，回复id不是非负
        self.assertEqual(reply_post_params_check("12345", -1), ("content", False))


if __name__ == '__main__':
    unittest.main()
