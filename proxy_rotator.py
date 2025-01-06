import requests
import time

# path to proxy file (make sure it's ur user)
proxy_file = 'C:/Users/test/Downloads/proxies/http.txt'

# Read proxies from file
def read_proxies():
    with open(proxy_file, 'r') as f:
        return [line.strip() for line in f if line.strip()]

# test it
def test_proxy(proxy):
    url = 'http://httpbin.org/ip'  # check with this url
    print(f"Trying {proxy}")
    
    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=30)
        if response.status_code == 200:
            print(f"Proxy {proxy} is good!")
            return True
    except requests.RequestException as e:
        print(f"Error with {proxy}: {e}")
    
    return False

# Rotate proxies
def rotate_proxies():
    proxies = read_proxies()
    if not proxies:
        print("No proxies found...")
        return
    
    for proxy in proxies:
        if test_proxy(proxy):
            break  # stop if proxy works
        else:
            print("Waiting 20 sec before next try...")
            time.sleep(20)  # pause before trying next proxy

if __name__ == "__main__":
    rotate_proxies()
