from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

global browser 

# Parameter 전송을 위한 Class 선언
class loginModule:    
    def __init__(self, userid, password):
        # 로그인
        self.userid = userid
        self.password = password

    def __del__(self):
        browser.quit()

    def login(self):
        global browser
        chrome_options = webdriver.ChromeOptions()

        # 브라우저 창 없이 실행
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu") 
        # 오류제어 추가
        chrome_options.add_argument("--no-sandbox")  # 대부분의 리소스에 대한 액세스를 방지 추가
        chrome_options.add_argument("--disable-setuid-sandbox") # 크롬 충돌을 막아줌 추가 
        chrome_options.add_argument("--disable-dev-shm-usage") # 메모리가 부족해서 에러가 발생하는 것을 막아줌 추가

        
        # Chromedriver 경로 설정
        browser = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_options)
    
        # url 이동
        browser.get("https://nlms.gwnu.ac.kr/login.php")

        # id, pw 입력 기존 방식과 다른 붙여넣기 방식으로 입력
        browser.execute_script("arguments[0].value=arguments[1]", browser.find_element(By.XPATH, '//*[@id="input-username"]'), self.userid) # 추가
        browser.execute_script("arguments[0].value=arguments[1]", browser.find_element(By.XPATH, '//*[@id="input-password"]'), self.password) # 추가

        # 로그인 버튼 클릭
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="region-main"]/div/div/div/div[1]/div[1]/div[2]/form/div[2]/input'))).click() # 변경

        # 버튼 클릭 이후 현재 URL 기반으로 성공 여부 체크
        if browser.current_url != 'https://nlms.gwnu.ac.kr/':
            return '-1'
        else:
            return '1'
    
# if __name__ == '__main__':
#     a = loginModule('20171473', '98031')
#     b = a.login()
#     print(b)