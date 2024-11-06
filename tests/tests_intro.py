from selenium.webdriver.common.by import By


def test_sauce_demo_title(driver, maximize_window, get_sauce_main_page):
    assert "Swag" in driver.title


def test_sauce_demo_login(driver, maximize_window, get_sauce_main_page):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url
