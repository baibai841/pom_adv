#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 11:24
# @Author  : huanghe
# @Site    : 
# @File    : test_create_ad_position_01.py
# @Software: PyCharm
import unittest
import os,sys
import logging
from baselib.logging.pylogging import setup_logging
from seleniumlib.browser import Browser, save_screenshot_file
from zq_lib.AquaPassAdv.login_page import LoginPage
from zq_lib.AquaPassAdv.first_page import FirstPage
from zq_lib.AquaPassAdv.ad_position import AdPostion
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from time import sleep
setup_logging()
#logger = logging.getLogger()

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = Browser(timeout=60)
        login_page = LoginPage(self.driver)
        login_page.url='http://10.50.4.115:8080/paasadv/'
        login_page.visit()
        login_page.wait(10)
        login_page.set_value(element=login_page.rec_user_input(),text="root")
        login_page.set_value(element=login_page.rec_passwd_input(),text="123")
        login_page.click_login_btn()
        self.first_page = login_page.get_first_page()

    def tearDown(self):
        self.driver.quit()


    def test_create_ad_position_01(self):
        #进入广告页面
        self.adposition_page = self.first_page.click_ad_position_btn()

        self.picture_page = self.adposition_page.click_picture_btn()
        self.create_ad_postion_for_picture = self.picture_page.click_create_btn()
        self.ad_id_input = self.create_ad_postion_for_picture.receive_ad_position_id_input()
        self.ad_name_input = self.create_ad_postion_for_picture.receive_ad_position_name_input()

        self.picture_width_input = self.create_ad_postion_for_picture.receive_size_width_input()

        self.picture_height_input = self.create_ad_postion_for_picture.receive_size_height_input()

        self.ad_number_input = self.create_ad_postion_for_picture.receive_ad_size_input()

        self.create_ad_postion_for_picture.set_value(self.ad_id_input, "003")
        self.create_ad_postion_for_picture.set_value(self.ad_name_input, u'新闻联播')
        self.create_ad_postion_for_picture.set_value(self.picture_width_input, "749")
        self.create_ad_postion_for_picture.set_value(self.picture_height_input, "477")
        self.create_ad_postion_for_picture.set_value(self.ad_number_input, "1")
        self.create_ad_postion_for_picture.select_match_suggest(u'可以拉伸')
        self.create_ad_postion_for_picture.select_default_ad(u'默认广告')
        sleep(0.5)
        self.create_ad_postion_for_picture.click_new_create_btn()

    if __name__ == '__main':
        unittest.main()