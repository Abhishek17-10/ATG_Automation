import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up logging
logging.basicConfig(filename="automation_log.txt", level=logging.INFO, format='%(asctime)s:%(message)s')
logging.info("====== WebDriver manager ======")

# Set up the WebDriver using WebDriver Manager
options = webdriver.ChromeOptions()
options.add_argument("--remote-debugging-port=9222")  # Enable browser logging
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the website
start_time = time.time()
driver.get("https://atg.party")
end_time = time.time()

# Log the status code and page load time
logging.info(f"Website is live. Status Code: {driver.execute_script('return document.readyState')}")
logging.info(f"Page load time: {end_time - start_time} seconds")

try:
    # Wait until the "LOGIN" link is clickable
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "LOGIN"))
    )
    login_button.click()
    logging.info("Login button clicked successfully.")

    # Wait for the login page to load
    time.sleep(2)

    # Fill in login credentials and log in
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    email_input.send_keys("wiz_saurabh@rediffmail.com")
    password_input.send_keys("Pass@123")
    password_input.send_keys(Keys.RETURN)

    # Wait for login to complete
    time.sleep(3)
    logging.info("Logged in successfully.")

    # Go to the article page
    driver.get("https://atg.party/article")

    # Wait for the article page to load
    time.sleep(2)

    # Fill in the title and description
    title_input = driver.find_element(By.ID, "title")
    description_input = driver.find_element(By.ID, "description")
    title_input.send_keys("Sample Article Title")
    description_input.send_keys("This is a sample description for the article.")

    # Upload a cover image
    image_path = "Image.jpg"  # Make sure image exists
    image_input = driver.find_element(By.ID, "cover_image")
    image_input.send_keys(image_path)
    logging.info("Cover image uploaded.")

    # Wait for TensorFlow Lite image processing to settle
    time.sleep(5)

    # Click on POST button
    post_button = driver.find_element(By.ID, "post")
    post_button.click()

    # Wait for the page to redirect
    time.sleep(5)

    # Log the URL of the new page
    new_url = driver.current_url
    logging.info(f"Article posted successfully. New page URL: {new_url}")

    # Check browser console logs for errors
    console_logs = driver.get_log("browser")
    for log in console_logs:
        logging.info(f"Console Log: {log}")

    #  Keep browser open for 15 minutes
    logging.info("Keeping browser open for 15 minutes.")
    time.sleep(900)

except Exception as e:
    logging.error(f"Error occurred: {e}")
    print("Error occurred. Check log for details.")

finally:
    # Close the browser
    driver.quit()
    logging.info("Browser closed.")
    print("Browser closed.")





