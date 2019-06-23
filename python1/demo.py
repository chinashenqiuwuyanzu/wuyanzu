
from appium import webdriver
from time  import sleep
# 建立与appium服务器需要的参数 以字典的形成
des={
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "emulator-5554",
  "appPackage": "com.tencent.tim",
  "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
  "noReset": "true",
  "unicodeKeyboard":"true",
  "resetKeyboard":"true"
}

# http://127.0.0.1:4723/wd/hub固定的  不需要改 或者localhost=127.0.0.1
# 测试脚本与appium服务器建立一个session连接
dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des)
sleep(5)
# # 第一步 先定义一个唯一的元素
# 第二步 在定义多个相同的元素
# dr.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱').clear()
# dr.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱').send_keys('465105918')
# sleep(5)
# # dr.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱').clear()
# dr.find_element_by_id('com.tencent.tim:id/password').send_keys('yaonulia123')
# sleep(3)
# dr.find_element_by_id('com.tencent.tim:id/login').click()
# sleep(3)
# items = dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.ImageView')
# sleep(1)
# print(items)

# for i in items:
# 	sleep(1)
# 	i.click()
# 	sleep(1)
# # 获取手机屏幕大小
# s = dr.get_window_size()
# # 放缩x，y轴
# x1=s['width']*0.5
# y1=s['height']*0.25
# y2=s['height']*0.75
# # 使用swipe方法 进行滑动操作
# dr.swipe(x1,y1,x1,y2)
# sleep(2)

# sleep(100)
# dr.quit()
# sleep(30)
# dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.FrameLayout')[-1].click()
# dr.find_elements_by_class_name('android.widget.RelativeLayout')
# dr.find_elements_by_class_name('android.widget.TextView')
# x=dr.find_elements_by_class_name('android.widget.ImageView')
# print(x)
# x[1].click()
# sleep(2)
# x[2].click()



# 导入模块
from HTMLTestReportCN import HTMLTestRunner
import unittest
from appium import webdriver
from time import sleep
import warnings


class DS(unittest.TestCase):

    # 每个用例执行之前运行一次，作用：用于清理测试环境残留数据，初始化测试环境
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.des = {
            "device": "android",
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "46HDU19314003325",
            "appPackage": "com.qk.butterfly",
            "appActivity": ".main.LauncherActivity",
            "noReset": "true",
        }
        # http://127.0.0.1:4723/wd/hub 固定的，写死localhost==127.0.0.1
        # 测试脚本与appium服务器建立一个session连接
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(5.0)

    # 写测试用例的部分
    def test_1(self):
        # 使用账号密码登录蝶声
        # 点击密码，进入手机号、密码登录页面
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        # 进入账号密码登录页面之后
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('18538097372')
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('dsound123456')
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()

        # 断言
        sleep(5.0)
        # 进入登录之后的页面
        a = self.dr.find_elements_by_id('com.qk.butterfly:id/tv_tab')[-1].text
        self.assertEqual(a, '我的',msg="断言已经登录成功")

    # 每个测试用例执行完毕之后，运行teardown一次，作用：测试用例运行完，清理测试环境

    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
