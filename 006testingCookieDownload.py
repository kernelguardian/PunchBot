try:
    import pickle
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=D:\\Works\\python\\selenium\\aestest\\") 
    
    browser = webdriver.Chrome('D:\\SETUPS\\chromedriver.exe', options=chrome_options)
    browser.get("http://www.aesajce.in")
    browser.get("https://www.aesajce.in/students/courseMaterials.php")
    input("Press enter to download cookies")
    browser.get("https://www.aesajce.in/students/courseMaterials.php")
    pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))
    pickle.dump( browser.get_cookies() , open("cookies.txt","wb"))
    print("cookies downloaded")
except Exception as e:
    input(e)
finally:
    print("Terminating")
    browser.quit()