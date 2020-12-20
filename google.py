import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
elem = driver.find_element_by_name("q")
# 검색창 찾는거 까지!
# 입력 어떻게하냐? send_keys
elem.send_keys("Pachycephalosaurus")
# 이제 엔터를 눌러야함!
elem.send_keys(Keys.RETURN)

# 이미지들 선택하기 전에 스크롤 부터 눌러서 쫙 선택하도록 하기
SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click() # 스크롤이 다 내려갔고 더보기 라는 버튼이 있을때 그버튼 클릭해서 이미지 뽑도록 하기
        except:
            break
    last_height = new_height
# =============================================
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
# 이제 다운받으려면 src 뒤에있는 주소를 가져와야 다운 가능
# n3VNCb
        time.sleep(1)
        imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")
# 클릭하고 이동할때는 브라우져도 시간이 필요함 그러므로 시간을 지연하는 코드 필요
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count = count + 1
    except:
        pass
driver.close()