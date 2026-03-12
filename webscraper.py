import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

search_url = "https://www.google.com/maps/search/pharmacy+in+guwahati/"
driver.get(search_url)
time.sleep(5)

# Scroll to load all listings
for _ in range(100):
    driver.execute_script(
        "document.querySelector('.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd').scrollBy(0, 1000);"
    )
    time.sleep(2)

results = []
cards = driver.find_elements(By.CLASS_NAME, "hfpxzc")

for card in cards:
    try:
        card.click()
        time.sleep(3)
        name = driver.find_element(By.CLASS_NAME, "DUwDvf").text
        try:
            website = driver.find_element(
                By.CSS_SELECTOR, "a[data-tooltip='Open website']"
            ).get_attribute("href")
        except:
            website = ""
        try:
            phone = driver.find_element(
                By.CSS_SELECTOR, "button[data-tooltip='Copy phone number']"
            ).text
        except:
            phone = ""
        try:
            address = driver.find_element(By.CLASS_NAME, "Io6YTe").text
        except:
            address = ""
        results.append(
            {
                "Name": name,
                "Website": website,
                "Phone": phone,
                "Address": address,
            }
        )
    except Exception as e:
        print("Error:", e)

df = pd.DataFrame(results)
df.to_csv("google_maps_pharmacies_guwahati.csv", index=False)

driver.quit()
