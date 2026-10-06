from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import re

driver = webdriver.Chrome()

driver.get("https://vinothqaacademy.com/demo-site/")

driver.maximize_window()

wait = WebDriverWait(driver, 20)


def js_click(element):
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        element
    )
    driver.execute_script(
        "arguments[0].click();",
        element
    )


try:

    first_name = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "vfb-5")
        )
    )
    first_name.send_keys("RAJARAMAN")

    last_name = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "vfb-7")
        )
    )
    last_name.send_keys("V")

    male = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//label[normalize-space()='Male']"
            )
        )
    )

    js_click(male)

    courses = [
        "Selenium WebDriver",
        "TestNG"
    ]

    for course in courses:
        checkbox = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//label[normalize-space()='{course}']"
                )
            )
        )

        js_click(checkbox)

    address_label = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//label[normalize-space()='Address']"
            )
        )
    )

    address_section = address_label.find_element(
        By.XPATH,
        "./ancestor::li[1]"
    )

    address_inputs = address_section.find_elements(
        By.XPATH,
        ".//input[not(@type='hidden')]"
    )

    address_inputs = [
        x for x in address_inputs
        if x.is_displayed() and x.is_enabled()
    ]

    address_inputs[0].send_keys("Saveetha clg")
    address_inputs[1].send_keys("saveetha nagae")
    address_inputs[2].send_keys("Flat 4B, Block A")
    address_inputs[3].send_keys("Thandalam")
    address_inputs[4].send_keys("600040")

    country = address_section.find_element(
        By.TAG_NAME,
        "select"
    )

    Select(country).select_by_visible_text("India")

    email = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "vfb-14")
        )
    )

    email.send_keys("rajaraman@example.com")

    date_label = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//label[contains(normalize-space(),'Date of Demo')]"
            )
        )
    )

    date_section = date_label.find_element(
        By.XPATH,
        "./ancestor::li[1]"
    )

    date = date_section.find_element(
        By.XPATH,
        ".//input[not(@type='hidden')]"
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        date
    )

    date.clear()
    date.send_keys("10/20/26")

    time_label = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//label[contains(normalize-space(),'Convenient Time')]"
            )
        )
    )

    time_section = time_label.find_element(
        By.XPATH,
        "./ancestor::li[1]"
    )

    time_selects = time_section.find_elements(
        By.TAG_NAME,
        "select"
    )

    Select(time_selects[0]).select_by_visible_text("10")
    Select(time_selects[1]).select_by_visible_text("30")

    mobile = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "vfb-19")
        )
    )

    mobile.send_keys("9940700636")

    query_label = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//label[contains(normalize-space(),'Enter your query')]"
            )
        )
    )

    query_section = query_label.find_element(
        By.XPATH,
        "./ancestor::li[1]"
    )

    query = query_section.find_element(
        By.TAG_NAME,
        "textarea"
    )

    query.send_keys(
        "I am learning Selenium automation testing."
    )

    verification_label = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//label[contains(normalize-space(),'Please enter two digits as displayed in Example')]"
            )
        )
    )

    verification_section = verification_label.find_element(
        By.XPATH,
        "./ancestor::li[1]"
    )

    example_text = verification_section.text

    match = re.search(
        r"Example:\s*(\d{2})",
        example_text
    )

    if match:
        verification_value = match.group(1)
    else:
        verification_value = "33"

    verification_inputs = verification_section.find_elements(
        By.XPATH,
        ".//input[not(@type='hidden')]"
    )

    verification_inputs = [
        x for x in verification_inputs
        if x.is_displayed() and x.is_enabled()
    ]

    verification_inputs[0].send_keys(
        verification_value
    )

    print("All details entered successfully.")

except Exception as e:
    print()
    print("ERROR:", type(e).__name__)
    print(e)

input("Browser is still open. Press Enter to close it...")
driver.quit()