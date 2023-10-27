import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = uc.ChromeOptions()
options.headless = False
driver = uc.Chrome(options=options)

# Navigate directly to the target site
driver.get("https://play.maisonmargiela.digital/game")

# Add your manually collected cookies here
cookies = [
    {
        "domain": ".maisonmargiela.digital",
        "expirationDate": 1729926141.186389,
        "hostOnly": false,
        "httpOnly": true,
        "name": "cf_clearance",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "YqD6TvmELrzX4HnF.ozG659kV5BwuZ1hRiAOaLLrnVw-1698390141-0-1-e8d15704.4ab447ec.bfd008e4-160.2.1698390141"
    },
    {
        "domain": ".maisonmargiela.digital",
        "expirationDate": 1698392913.413919,
        "hostOnly": false,
        "httpOnly": true,
        "name": "__cf_bm",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "s4x.4Z6VxveQs23AKxd7caaQsd3RHXXgcdpTB_sy.lk-1698391113-0-AWrt0foKWUu5jdDksjBMY8DoxObrdyEV0IySkqEEEcEhC9YIUhMwYI2Y0Ptcd4GOFaXuVn8QMm32gKgsmPOkTBc="
    }
]

# Add cookies
for cookie in cookies:
    driver.add_cookie(cookie)

# Refresh the page after setting the cookies
driver.refresh()

# Define the full XPATH of the button
button_xpath = '/html/body/div[1]/main/div[2]/div[2]/div[2]/button[2]'

try:
    # Wait for the button to be available and then click it
    button = WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.XPATH, button_xpath)))
    button.click()
except Exception as e:
    print(f"An error occurred: {e}")
    # Keeping the browser open for troubleshooting
    input("Press Enter to close the browser...")
    driver.quit()
