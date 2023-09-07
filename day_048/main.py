"""
The Cookie Clicker Project by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules/libraries #######
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Declare constant/global variables
URL = "http://orteil.dashnet.org/experiments/cookie/"


# Main #######
def main():
    # Create webdriver instance and configure
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(URL)

    # Locate cookie to click
    cookie = driver.find_element(By.CSS_SELECTOR, value="div#cookie")

    # Obtain and locate upgrades
    ups = driver.find_elements(By.CSS_SELECTOR, value="div#store div")
    ups_list = [up.get_attribute("id") for up in ups]
    ups_raw = [up.find_element(By.CSS_SELECTOR, value="b").text for up in ups][:-1]
    ups_prices = [int(up.split("-")[1].strip().replace(",", "")) for up in ups_raw]
    cookie_ups = {ups_prices[x]: ups_list[x] for x in range(len(ups_prices))}

    print(cookie_ups)

    # Define time variables
    timeout = time.time() + 5
    five_min = time.time() + 300

    # main program loop
    while True:
        cookie.click()

        # Every 5 seconds
        if time.time() > timeout:
            # Get current cookie_count
            money_elem = driver.find_element(By.CSS_SELECTOR, value="div#money").text
            if "," in money_elem:
                money_elem = money_elem.replace(",", "")
            cookie_count = int(money_elem)

            # Find affordable upgrades
            affordable_ups = {}
            for cost, id in cookie_ups.items():
                if cookie_count >= cost:
                    affordable_ups[cost] = id

            # Purchase the most expensive from the most affordable upgrade list
            highest = max(affordable_ups)
            to_purchase_id = affordable_ups[highest]
            driver.find_element(By.ID, value=to_purchase_id).click()

            # Add another 5 seconds until next check
            timeout = time.time() + 5

        if time.time() > five_min:
            print(driver.find_element(By.ID, value="cps").text)
            break

    driver.quit()


# Run program
if __name__ == "__main__":
    main()
