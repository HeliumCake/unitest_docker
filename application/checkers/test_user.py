import unittest
from .user import register_params_check


class UserCheckTest(unittest.TestCase):
    def test_example(self):
        # 正确输入
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("ok", True))

    def test_example_2(self):
        # 缺失用户账号
        user = {
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("username", False))

    def test_example_3(self):
        # 缺失用户密码
        user = {
            'username': 'username',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("password", False))

    def test_example_4(self):
        # 缺失用户昵称呢
        user = {
            'username': 'username',
            'password': 'Password123',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("nickname", False))

    def test_example_5(self):
        # 缺失用户身份证号
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("document_number", False))

    def test_example_6(self):
        # 缺失手机号
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("mobile", False))

    def test_example_7(self):
        # 缺失邮箱信息
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
        }
        self.assertEqual(register_params_check(user), ("email", False))

    def test_example_8(self):
        # 用户账号长度小于6
        user = {
            'username': 'usern',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("username", False))

    def test_example_9(self):
        # 用户账号长度大于10
        user = {
            'username': 'username901',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("username", False))

    def test_example_10(self):
        # 用户密码长度小于6
        user = {
            'username': 'username',
            'password': 'Pa123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("password", False))

    def test_example_11(self):
        # 用户密码长度大于18
        user = {
            'username': 'username',
            'password': 'Password12345678901',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("password", False))

    def test_example_12_(self):
        # 用户密码包含非字母和数字的字符
        user = {
            'username': 'username',
            'password': 'Password123!',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("password", False))

    def test_example_12(self):
        # 用户密码不包含大写字母
        user = {
            'username': 'username',
            'password': 'password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("password", False))

    def test_example_13(self):
        # 用户密码不包含小写字母
        user = {
            'username': 'username',
            'password': 'PASSWORD123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("password", False))

    def test_example_14(self):
        # 用户密码不包含数字
        user = {
            'username': 'username',
            'password': 'Password',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("password", False))

    def test_example_15(self):
        # 用户昵称长度小于2
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'n',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("nickname", False))

    def test_example_16(self):
        # 用户昵称长度大于8
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname1',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("nickname", False))

    def test_example_17_(self):
        # 用户身份证号包含非数字的字符
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '11111!200011110007',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("document_number", False))

    def test_example_17(self):
        # 用户身份证号长度小于18位
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '11111200011110007',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("document_number", False))

    def test_example_18(self):
        # 用户身份证号长度大于18位
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '1111111200011110008',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("document_number", False))

    def test_example_19(self):
        # 用户身份证号校验码不正确
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110001',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("document_number", False))

    def test_example_20(self):
        # 用户身份证号出生日期不存在，无13月
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200013110004',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("document_number", False))

    def test_example_21(self):
        # 用户身份证号出生日期不存在，无4月31日
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200004310004',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("document_number", False))

    def test_example_22(self):
        # 用户身份证号出生日期不存在，无1999年2月29日
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111199902290003',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("document_number", False))

    def test_example_23(self):
        # 用户身份证号出生日期不存在，无1900年2月29日
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111190002290007',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("document_number", False))

    def test_example_24(self):
        # 正确输入，存在2000年2月29日
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200002290003',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("ok", True))

    def test_example_25(self):
        # 用户未年满18周岁
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200211110005',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("document_number", False))

    def test_example_26(self):
        # 手机号长度小于11位
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 1234567890,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("mobile", False))

    def test_example_27(self):
        # 手机号长度大于11位
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 123456789012,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("mobile", False))

    def test_example_28(self):
        # 邮箱信息不包含'@'
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email123.email'
        }
        self.assertEqual(register_params_check(user), ("email", False))

    def test_example_29(self):
        # 邮箱信息包含多个'@'
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@1@23.email'
        }
        self.assertEqual(register_params_check(user), ("email", False))

    def test_example_30(self):
        # 邮箱信息没有域内部分
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': '@123.email'
        }
        self.assertEqual(register_params_check(user), ("email", False))

    def test_example_31(self):
        # 邮箱信息没有域名
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@'
        }
        self.assertEqual(register_params_check(user), ("email", False))

    def test_example_32(self):
        # 邮箱信息域内部分长度大于63
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': '1234567890123456789012345678901234567890123456789012345678901234@123.email'
        }
        self.assertEqual(register_params_check(user), ("email", False))

    def test_example_33(self):
        # 邮箱信息域内含有不是字母和数字的字符
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email.@123.email'
        }
        self.assertEqual(register_params_check(user), ("email", False))

    def test_example_34(self):
        # 邮箱信息域名长度大于63
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123456789012345678901234567890123456789012345678901234567890.email'
        }
        self.assertEqual(register_params_check(user), ("email", False))

    def test_example_35(self):
        # 邮箱信息域名含有不是字母、数字、连字符、点的字符
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123!.email'
        }
        self.assertEqual(register_params_check(user), ("email", False))

    def test_example_36(self):
        # 邮箱信息域名最后一段顶级域名是纯数字
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.123'
        }
        self.assertEqual(register_params_check(user), ("email", False))

    def test_example_37(self):
        # 邮箱信息域名连字符作为首字符
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@-123.email'
        }
        self.assertEqual(register_params_check(user), ("email", False))

    def test_example_38(self):
        # 邮箱信息域名连字符作为尾字符
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123-.email'
        }
        self.assertEqual(register_params_check(user), ("email", False))

    def test_example_39(self):
        # 用户账号不是字符串
        user = {
            'username': 12345,
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("username", False))

    def test_example_40(self):
        # 用户密码不是字符串
        user = {
            'username': 'username',
            'password': 123456,
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("password", False))

    def test_example_41(self):
        # 用户昵称不是字符串
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 123456,
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("nickname", False))

    def test_example_42(self):
        # 用户身份证号不是字符串
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': 111111200011110000,
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("document_number", False))

    def test_example_43(self):
        # 手机号不是数字
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': '12345678901',
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("mobile", False))

    def test_example_44(self):
        # 邮箱信息不是字符串
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '111111200011110000',
            'mobile': 12345678901,
            'email': 123456
        }
        self.assertEqual(register_params_check(user), ("email", False))

    def test_example_45(self):
        # 正确输入，且身份证校验码为X
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '11111120001101000X',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("ok", True))

    def test_example_46(self):
        # 用户身份证号校验码不正确，且身份证校验码为X
        user = {
            'username': 'username',
            'password': 'Password123',
            'nickname': 'nickname',
            'document_number': '11111120001111000X',
            'mobile': 12345678901,
            'email': 'email@123.email'
        }
        self.assertEqual(register_params_check(user), ("document_number", False))

    def test_example_47(self):
        # 类型错误
        self.assertEqual(register_params_check(None), ("username", False))


if __name__ == '__main__':
    unittest.main()
