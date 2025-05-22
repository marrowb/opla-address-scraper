import requests
from bs4 import BeautifulSoup
import json


def get_opla_offices():
    opla_offices = []
    
    for page in range(4):
        url = f"https://www.ice.gov/contact/field-offices?state=All&office=12&keyword=&page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        offices = soup.find_all('li', class_='grid')
        
        for office in offices:
            name = office.find('span', class_='field-content').text
            locality = office.find('span', class_='city').text
            
            if 'Mailing Address' in office.text:
                mailing_addr = office.find('p')
                if 'Mailing Address' in mailing_addr.text:
                    addr_lines = mailing_addr.text.split('\n')
                    address_line_1 = addr_lines[0]
                    suite = addr_lines[1]
                    city_state_zip = addr_lines[2]
                    opla_offices.append({
                        "locality": locality,
                        "name": name,
                        "address_line_1": address_line_1,
                        "suite": suite,
                        "city_state_zip": city_state_zip
                    })
            else:
                address_line_1 = office.find('span', class_='address-line1').text
                city = office.find('span', class_='locality').text
                state = office.find('span', class_='administrative-area').text
                zipcode = office.find('span', class_='postal-code').text
                city_state_zipcode = f"{city}, {state} {zipcode}"
                opla_offices.append({
                    "locality": locality,
                    "name": name,
                    "address_line_1": address_line_1,
                    "city_state_zip": city_state_zipcode
                })
    
    return opla_offices


if __name__ == "__main__":
    opla_offices = get_opla_offices()
    
    with open("opla_office_addresses.json", "w") as f:
        json.dump(opla_offices, f, indent=4, ensure_ascii=False)
    
    import IPython
    IPython.embed()
