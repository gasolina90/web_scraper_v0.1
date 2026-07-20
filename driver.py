from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    element_list = []

    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Use a Service object
    service = Service(ChromeDriverManager().install())

if __name__ == "__main__":
    main()