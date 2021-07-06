from src.util.constants import logger

import netifaces as ni

import platform, traceback

def Get_IP_Address():
    # This is a trick that I use when I switch from Linux(RHEL) based servers and my local macbook
     logger.info("Application running on Platform: [{}]".format(platform.platform()), extra={"logname" : "SYSTEM"})
     if any(substring in platform.platform() for substring in ['mac', 'Darwin']):
         return ni.ifaddresses('en0')[ni.AF_INET][0]['addr']
     else:
         return ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']


def Check_Annual_Income_In_Tax_Bracket(annual_income, tax_bracket):
    try:
        if "max" in tax_bracket:
            if annual_income <= tax_bracket['max'] and annual_income > tax_bracket['min']:
                return True
            elif annual_income == 0:
                return True
            else: return False
        
        else:
            if annual_income >= tax_bracket['min']:
                return True
            else: return False
    except Exception:
        logger.info("An error occurred during Check_Annual_Income_In_Tax_Bracket")
        logger.error(traceback.print_exc())