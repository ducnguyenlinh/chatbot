from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class Coronavirus:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    def get_data(self):
        self.driver.get('https://www.worldometers.info/coronavirus/')
        table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]')
        country_element = table.find_element_by_xpath("//td[contains(., 'Japan')]")
        row = country_element.find_element_by_xpath("./..")
        data = row.text.split(" ")
        total_cases = data[2]
        new_cases = data[3]
        total_deaths = data[4]
        new_deaths = data[5]
        active_cases = data[6]
        total_recovered = data[7]
        serious_critical = data[8]

        status = "Total cases: " + total_cases + "\n"
        status += "New cases: " + new_cases + "\n"
        status += "Total deaths: " + total_deaths + "\n"
        status += "New deaths: " + new_deaths + "\n"
        status += "Active cases: " + active_cases + "\n"
        status += "Total recovered: " + total_recovered + "\n"
        status += "Serious, critical cases: " + serious_critical + "\n"

        self.driver.close()
        self.driver.quit()

        return status
