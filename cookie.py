from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import time

URL = "http://orteil.dashnet.org/experiments/cookie/"
chrome_driver_path = "F:/replit/day-48/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
each_element = []
each_element_again = []
turn = True
max_turn = True
count = 0
cost_id = {}
# item_ids =[]


class Upgrade:
    def game(self):
        items = driver.find_elements_by_css_selector("#store div")
        item_ids = [item.get_attribute("id") for item in items if item.get_attribute("id") != ""]
        print(item_ids)

        require = driver.find_elements_by_css_selector("#store b")
        for element in require:
            if element.text != "":
                running_no = (element.text.split(" - ")[1].replace(",", ""))
                each_element.append(int(running_no))
        print(each_element)

        for n in range(len(each_element)):
            cost_id[each_element[n]] = item_ids[n]
        print(cost_id)

        del each_element[:]
        del item_ids[:]

    # def __init__(self, new_value):
    #     self.new_value = new_value

    def purchase(self, new_value):
        require_again = driver.find_element_by_id(cost_id[new_value])
        require_again.click()
        cost_id.clear()
        # for element_again in require_again:
        #     if element_again.text != "":
        #         each_element_again.append(element_again.text.split(" - ")[0])
        # print(type(each_element_again))


upgrade = Upgrade()

while turn:
    cookie = driver.find_element_by_id("cookie")
    points = driver.find_element_by_id("money")
    max_turn = True
    upgrade.game()
    time_out = time() + 5
    count = count + 1

    while time() <= time_out:
        cookie.click()

    # max_num = max(each_element)
    # print(max_num)
    while max_turn:
        max_num = max(cost_id)
        point = (points.text).replace(",", "")
        # asd = point.replace(",", "")
        if max_num <= int(point):
            print(point)
            max_turn = False
        else:
            del cost_id[max_num]

    max_num = max(cost_id)
    print(max_num)
    upgrade.purchase(new_value=max_num)

    if count == 60:
        turn = False
    # del each_element[:]
    # del item_ids[:]
# print(points.text)


