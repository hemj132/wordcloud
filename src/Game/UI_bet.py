#coding=utf-8
from selenium import webdriver
import sys
import time
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait                            # available since 2.4.0
# from selenium.webdriver.support import expected_conditions as EC
reload(sys)
sys.setdefaultencoding('utf8')

class UIbet:
    def __init__(self):

        self.url="http://member.iwc678.com/#/login"

        self.browser = webdriver.Chrome()

        self.browser.get( self.url)
        self.browser.maximize_window()
        self.browser.implicitly_wait(30)
        #self.wait = WebDriverWait(self.browser, 10)

    def login(self,username,pwd):
        input_user=self.browser.find_elements_by_id("account")[1]

        input_user.send_keys(username)
        input_pwd=self.browser.find_element_by_id("password")
        input_pwd.send_keys(pwd)
        input_code = self.browser.find_element_by_id("code")
        #获取骗自己得验证码
        code=''
        for i in range(1,5):
            code+=self.browser.find_element_by_xpath('//div[@class="verification-code"]/div['+str(i)+']').text
        input_code.send_keys(code)

        #login_butten=self.browser.find_element_by_class_name("ant-btn login-form-button ant-btn-primary")
        login_butten=self.browser.find_element_by_xpath('//button[@type="button"]')
        login_butten.click()
        yes_butten=self.browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/button[1]')

        yes_butten.click()

    #lotterys彩种位置list
    def bet(self,lotterys,amount):
        #最开始没有确认弹窗,弹窗XPATH绝对位置
        confirm_times=0
        for lottery in lotterys:
            tips_lottery=self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/ul/li[{0}]'.format(lottery))
            print tips_lottery.is_enabled()
            #点到不报错为止
            flag=False
            while (flag == False):
                time.sleep(0.5)
                flag = self.isElementClick(tips_lottery)
            #tips_lottery.click()
            lottery_name=tips_lottery.text
            #print lottery_name
            try:
                self.browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/ul/li[1]').click()
            except:

                print lottery_name + " 今天没有开盘"

                #两名盘+数值盘
            else:
                for i in range(1,3):
                    try:
                        self.browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/ul/li[{0}]'.format(i)).click()
                    except:
                        print lottery_name + " 今天没有开盘"
                        continue
                    iput_vluse=self.browser.find_element_by_xpath('//div[@class="bets-amount"]/input')
                    #已经封盘
                    if iput_vluse.get_attribute("value")!='':
                        #获取开奖时间
                        times=int(self.browser.find_elements_by_class_name("time-frame")[2].text)*60+int(self.browser.find_elements_by_class_name("time-frame")[3].text)
                        print times
                        time.sleep(times+5)

                    #全选
                    self.browser.find_element_by_xpath('//div[@class="bets-amount"]/button').click()
                iput_vluse.send_keys(amount)
                    #下注
                self.browser.find_element_by_xpath('//div[@class="bets-buttons"]/div[2]').click()
                    #确认
                time.sleep(3)
            #确认弹框每次出来+1

                self.browser.find_elements_by_xpath('//div[@class="submit-footer"]/div[2]')[confirm_times].click()
            # self.browser.find_element_by_xpath('/html/body/div[{}]/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[2]'.format(confirm_times)).click()
                confirm_times += 1
            # '/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[2]'

                #self.wait.until(EC.presence_of_located(By.XPATH,'/html/body/div[4]/div/span/div/div/div/div[2]'))
                #self.wait.until(EC.presenceOfElementLocated(By.xpath()))




            #else:

    def isElementClick(self, tips_lottery):
        flag = False

        try:
            tips_lottery.click()
            flag = True
            return flag

        except:

            return flag



if __name__ == '__main__':
    lotterys=[1,2,3,4,5,6,7,8,9]
    bet=UIbet()
    bet.login("TESTL6P0R0O0N1","qwe123")
    bet.bet(lotterys,100)