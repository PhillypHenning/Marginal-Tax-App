from src.util.constants import *
from src.util.utilities import Check_Annual_Income_In_Tax_Bracket

from flask import jsonify, request, Blueprint

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

import requests, traceback

process_incometax_blueprint = Blueprint('calculateincometax', __name__,)

retry_strategy = Retry(
    total=RETRY_TIMES,
    status_forcelist=RETRY_ON_CODES,
    allowed_methods=RETRY_ON_METHODS
)

adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)


@process_incometax_blueprint.route("/calculate/incometax")
def process_incometax():
    callers_id = request.remote_addr
    logger.info("Process Income Tax started for IP Address: [{}]".format(callers_id))

    year = request.args.get("year")
    annual_income = request.args.get("annual income")

    try:
        year = int(year)
        annual_income = float(annual_income)
    except ValueError as e:
        logger.warning("An error occured while converting query params")
        logger.error(traceback.print_exc())
        msg = {"Message": "Not Okay", "Error": "Supplied Query Params"}
        return jsonify(msg), 409

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
            try:
                bracket = ITD[index]            
                # Get the Amount taxed by taking bracket amount and multiplying by rate
                tax_from_bracket_due = taxable_income * bracket['rate']
                # Total up the taxed income
                taxed_income = taxed_income + tax_from_bracket_due

                #logger.info("Annual Amount: [{}] | Annual Amount left to tax: [{}] | Taxes paid: [{}] | Tax rate of: [{}] | Total Tax Paid: [{}]".format(annual_income, taxable_income, taxed_income, bracket['rate'], tax_from_bracket_due))
                
                tax_info = {'Total Federal Taxes:': float("{:.2f}".format(taxed_income))}
                break
            
            except Exception as e:
                logger.warning("An error occured while processing IP: [{}]".format(callers_id))
                logger.error(traceback.print_exc())
        
        else:           
            # Annual Amount - "max" amount
            # Max amount * Rate = tax_from_bracket_due
            # MAX - MIN = BRACKET RANGE
            
            try:
                bracket = ITD[index]

                income_taxable_range = int(bracket['max']) - int(bracket['min'])
                # No need to worry about finding the total amount being taxed as these brackets are fully 'covered' by the annual amount            
                tax_from_bracket_due = income_taxable_range * bracket['rate']
                taxed_income = taxed_income + tax_from_bracket_due

                #logger.info("Annual Amount: [{}] | Annual Amount left to tax: [{}] | Taxes paid: [{}] | Tax rate of: [{}] | Total Tax Paid: [{}]".format(annual_income, taxable_income, taxed_income, bracket['rate'], tax_from_bracket_due))

                taxable_income = taxable_income - income_taxable_range
                index=index+1
            except Exception as e:
                logger.warning("An error occured while processing IP: [{}]".format(callers_id))

    logger.info("Process Income Tax Finished for IP Address: [{}]".format(callers_id))

    msg = tax_info | {"Year": year, "Annual Income": annual_income}
    return jsonify(msg)