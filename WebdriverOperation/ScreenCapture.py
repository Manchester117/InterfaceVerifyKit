# -*- coding: utf-8 -*-
__author__ = 'Peng.Zhao'

from selenium import webdriver
from EmailNotice import SendEmail

import time


def web_driver_screen_capture():
    driver = webdriver.Firefox()
    # 获取最新的一份儿报告
    new_report = SendEmail.select_report("ReportAndLog/Report/")
    driver.get("file:///D:/PythonWorkSpace/HighPin_VIK/ReportAndLog/Report/" + new_report)
    time.sleep(1)
    # 截取报告的HTML后缀,用于图片命名
    new_report = new_report[:-5]
    driver.get_screenshot_as_file("ReportAndLog/ScreenCapture/" + new_report + ".png")
    time.sleep(1)
    driver.quit()

