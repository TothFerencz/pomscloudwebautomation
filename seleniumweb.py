from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Weboldal megnyitása
    driver.get("https://www.npmjs.com/")

    # Keresőmező kiválasztása és kifejezés beírása
    search_input = driver.find_element(By.XPATH, "//input[@placeholder='Search packages']")
    search_input.send_keys("express")
    search_input.send_keys(Keys.RETURN)

    # Első találat kiválasztása
    first_result_xpath = "//h3[contains(text(),'express')]"
    first_result = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, first_result_xpath))
    )
    first_result.click()

    # Győződjünk meg arról, hogy az oldal betöltődött
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//body"))
    )

    # az expressjs csomag legfrissebb verzióját feljegyezzük
    version_element_xpath = "//span[contains(@class, '_76473bea') and contains(@class, 'f6') and contains(@class, 'dib') and contains(@class, 'ph0') and contains(@class, 'pv2') and contains(@class, 'mb2-ns') and contains(@class, 'black-80') and contains(@class, 'nowrap') and contains(@class, 'f5') and contains(@class, 'fw4') and contains(@class, 'lh-copy')]"
    version_element = driver.find_element(By.XPATH, version_element_xpath)
    latest_version = version_element.text

    # Kiírás a konzolra
    print("A legfrisebb verzió:", latest_version)
finally:
    # Böngésző bezárása
    driver.quit()
