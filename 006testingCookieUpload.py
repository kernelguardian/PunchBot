try:
    import pickle
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=D:\\Works\\python\\selenium\\aestest\\") 
    
    browser = webdriver.Chrome('D:\\SETUPS\\chromedriver.exe', options=chrome_options)
    browser.get('http://www.aesajce.in') #Dummy page to load the cookies first
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.get("https://www.aesajce.in/students/courseMaterials.php")
    input('Waiting for input')
except Exception as e:
    input(e)
finally:
    print("Terminating")
    browser.quit()
