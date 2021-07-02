from flask import Flask, jsonify, request
from src.util.constants import *

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

import netifaces as ni

import platform, requests

app = Flask(__name__)

retry_strategy = Retry(
    total=5,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "GET", "OPTIONS"]
)

adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)

## UTILITIES ##
def Get_IP_Address():
     logger.info("Application running on Platform: [{}]".format(platform.platform()), extra={"logname" : "SYSTEM"})
     if any(substring in platform.platform() for substring in ['mac', 'Darwin']):
         return ni.ifaddresses('en0')[ni.AF_INET][0]['addr']
     else:
         return ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']


def Check_Annual_Income_In_Tax_Bracket(annual_income, tax_bracket):
    #if annual_income < ITD[mid_index]['max'] and annual_income >= ITD[mid_index]['min']:
    if "max" in tax_bracket:
        if annual_income <= tax_bracket['max'] and annual_income > tax_bracket['min']:
            return True
        else: return False
    else:
        if annual_income >= tax_bracket['min']:
            return True
        else: return False


## ROUTES ##
@app.route("/healthcheck")
def health_check():
    return jsonify({"Message": "Okay"})

@app.route("/calculate/incometax")
def process_incometax():
    year = int(request.args.get("year"))
    annual_income = float(request.args.get("annual income"))

    # Confirm that the supplied year is valid
    if year not in VALID_YEARS:
        msg = {"Message": "Not Okay", "Year": year, "Error": "Supplied year isn't valid. Valid years; [{}]".format(VALID_YEARS)}
        logger.warning(msg)
        return jsonify(msg), 401
    
    # Make a request to the CTB Server with the supplied year
    address = "{}/{}/{}".format(CTB_API_URL, CTB_API_ROUTE, year)

    response = http.get(address)
    income_tax_data = response.json() 

    ITD = income_tax_data['tax_brackets']
    tax_info = None
    index = 0
    taxable_income = annual_income
    taxed_income = 0

    while index != len(ITD)-1:
        if Check_Annual_Income_In_Tax_Bracket(annual_income, ITD[index]):
            
            bracket = ITD[index]            
            # Get the Amount taxed by taking bracket amount and multiplying by rate
            tax_from_bracket_due = taxable_income * bracket['rate']
            # Total up the taxed income
            taxed_income = taxed_income + tax_from_bracket_due

            logger.info("Annual Amount: [{}] | Annual Amount left to tax: [{}] | Taxes paid: [{}] | Tax rate of: [{}] | Total Tax Paid: [{}]".format(annual_income, taxable_income, taxed_income, bracket['rate'], tax_from_bracket_due))
            
            tax_info = {'Total Federal Taxes:': float("{:.2f}".format(taxed_income))}
            break
        
        else:            
            # Annual Amount - "max" amount
            # Max amount * Rate = tax_from_bracket_due
            # MAX - MIN = BRACKET RANGE
            bracket = ITD[index]

            income_taxable_range = int(bracket['max']) - int(bracket['min'])
            # No need to worry about finding the total amount being taxed as these brackets are fully 'covered' by the annual amount            
            tax_from_bracket_due = income_taxable_range * bracket['rate']
            taxed_income = taxed_income + tax_from_bracket_due

            logger.info("Annual Amount: [{}] | Annual Amount left to tax: [{}] | Taxes paid: [{}] | Tax rate of: [{}] | Total Tax Paid: [{}]".format(annual_income, taxable_income, taxed_income, bracket['rate'], tax_from_bracket_due))

            taxable_income = taxable_income - income_taxable_range
            index=index+1
    
    msg = tax_info | {"Year": year, "Annual Income": annual_income}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host=Get_IP_Address(), port=4000)