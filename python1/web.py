# from selenium import webdriver
# from time import sleep
# # from selenium.webdriver.common.action_chains import ActionChains
# # import selenium.webdriver.support.ui as  ui
# dr = webdriver.Chrome()
# dr.get('https://www.alltuu.com/')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/ul/li[2]/div/a[1]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/section[2]/div/input').send_keys('17826808915')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/section[3]/div/input').send_keys('123789')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/section[4]/div').click()
# sleep(2)
# dr.find_element_by_xpath('').click()


# from selenium import webdriver
# import unittest
# import time
#
#
#
# class MyTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#         self.base_url = "http://www.baidu.com"
#
#     def test_baidu(self):
#         driver = self.driver
#         driver.get(self.base_url + "/")
#         driver.find_element_by_id("kw").clear()
#         driver.find_element_by_id('kw').send_keys('unittest')
#         driver.find_element_by_id('su').click()
#         time.sleep(2)
#         title = driver.title
#         self.assertEqual(title, 'unittest_百度搜索')
#
#     def tearDown(self):
#         self.driver.quit()
#
#
# if __name__ == "__main__":
#     unittest.main()





from selenium import webdriver
from time import sleep
import unittest
class wutu(object):
    def  wangzhi(self):
        self.dr = webdriver.Firefox()
        self.dr.get('https://www.alltuu.com/')
    #     sleep(2)
    # def  wuying(self):
    #     dr = self.dr
    #     tt = dr.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[2]/p[1]')
    #     print(tt)
        # self.assertEqual(title,'untitles_喔图云摄影')
if __name__ == "__main__":
    wutu().wangzhi()





























# sleep(2)      10 最大等待时间
# 创建一个智能等待
# unitl = ui.WebDriverWait(dr,10)
# # 如果定位的元素出现了就不必在等待
# unitl.until(lambda dr: dr.find_element_by_link_text('hao123').is_displayed())
# # 检测hao123这个文本是否出现了   如果出现了就执行下面的代码   如果没有出现就等待10秒
#
# dr.find_element_by_link_text('新闻').click()
# # sleep(2)
# print(unitl)



# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_id("switcher_plogin").click()
# sleep(2)
# dr.find_element_by_id('u').send_keys('465105918')
# sleep(2)
# dr.find_element_by_id('p').send_keys('')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# ww =  dr.find_elements_by_class_name('mnav')
# for i in ww:
#     b = i.get_attribute('name')
#     # 获取某个属性的值
#     print(b)
# dr.find_element_by_id('J_roomCountList').find_element_by_tag_name('option')
# 模拟鼠标移动
# ww = dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_class_name('cate_menu_lk')
# # ActionChains(dr).move_to_element(ww).perform()
# # sleep(3)
# for i in ww:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(6)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(3)
# # dr.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('18765827')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('asdf')
# sleep(2)
#
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# dr.switch_to.frame('tcaptcha_iframe')
# cc = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
# ActionChains(dr).drag_and_drop_by_offset(cc,170,0).perform()
# drag_and_drop 接收到俩个参数（起始位置，结束位置）
# drag_and_drop_by_offset 接收到三个参数 （起始位置，x轴坐标，y轴坐标）


# qq = 'var q=document.documentElement.scrollTop=10000'
# 执行JavaScript语句
# dr.execute_script(qq)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# sleep(2)
# # 获取窗口号
# aa = dr.window_handles
# sleep(2)
# print(aa)
# # 切换窗口
# dr.switch_to.window(aa[-1])
# print(dr.title)

# # 处理弹出框
# dr.find_element_by_xpath('/html/body/input').click()
# sleep(2)
# # 切换到弹出框上面去
# ww = dr.switch_to_alert()
# # 获取弹出框上面的确定
# print(ww.text)
# # 点击确定
# ww.accept()
# # 点击取消
# ww.dismiss();
