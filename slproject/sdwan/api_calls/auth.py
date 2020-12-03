import requests
import json

def login():
    baseurl = "https://10.100.99.28:8443"
    authentication_endpoint = "/j_security_check"
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    body = {    
        "j_username": "admin",
        "j_password": "!!!C1sco123!!!",
    }

    session = requests.session()
    requests.packages.urllib3.disable_warnings()

    url = f"{baseurl}{authentication_endpoint}"
    login_response = session.post(url, data=body, verify=False)

    if b'<html>' in login_response.content:
        #print("Login Failed")
        import sys
        sys.exit(0)
    else:
        #print("Login succeeded")
        return session
                
if __name__ == "__main__":
   response = login()
   print(response)