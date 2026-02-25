from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

columns_name = ["World Rank", "National Rank", "Name", "Affiliation", "Country", "H-Index", "Citations", "#DBLP", "Image URLs"]

def get_scholar_details(information):
    details = information.text.split('\n')
    #print(details)

    contents = {}
    contents["World Rank"] = details[0]
    contents["National Rank"] = details[1]
    contents["Name"] = details[2]
    contents["Affiliation"] = details[3].split(",")[0]
    contents["Country"] = details[3].split(",")[1].strip()
    contents["H-Index"] = details[4]
    contents["Citations"] = details[5].replace(',','')
    contents["#DBLP"] = details[6].repalce(',', '')
    contents["Image URLs"] = information.find_element(By.CSS_SELECTOR, "span.img img").get_attribute("src")
    #print(contents[0])
    return contents

#def make_dataframe(tables):
    #df = pd.DataFrame(data=tables, columns= columns_name)
    #df.head()
    

def main():
    scholar_data = []
    driver = webdriver.Chrome()
    for page in range(1, 11):
        url = f"https://research.com/scientists-rankings/computer-science?page={page}"
        driver.get(url)
        time.sleep(10)
        rankings = driver.find_element(By.CLASS_NAME, "rankings-content")
    
        # rows data need for dataframe
        rows = rankings.find_elements(By.CLASS_NAME, "scientist-item")

        for idx, row in enumerate(rows):
            scholar_data.append(get_scholar_details(row))
    driver.close()
    #print(scholar_data[0])
    #print(len(scholar_data))

    df = pd.DataFrame(data=scholar_data, columns=columns_name)
    df.to_csv("Best_CS_Scientist.csv", index=False)
    return 

if __name__ == "__main__":
    main()