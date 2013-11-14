import balanced

balanced.configure('ak-test-14W5azoiV99O1XiPwZ3faH10MaUdZ1kCA')

merchant_data = {
    "phone_number": "+140899188155", 
    "name": "Skripts4Kids", 
    "person": {
        "dob": "1989-12", 
        "phone_number": "+14089999999", 
        "postal_code": "94110", 
        "name": "Timmy Q. CopyPasta", 
        "street_address": "121 Skriptkid Row"
    }, 
    "postal_code": "91111", 
    "type": "business", 
    "street_address": "555 VoidMain Road", 
    "tax_id": "211111111"
}

account = balanced.Account().save()

try:
    account.add_merchant(merchant_data)
except balanced.exc.MoreInformationRequiredError as ex:
    # could not identify this account.
    print 'redirect merchant to:', ex.redirect_uri
except balanced.exc.HTTPError as error:
    # TODO: handle 400 and 409 exceptions as required
    raise