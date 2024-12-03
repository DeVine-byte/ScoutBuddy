import requests
from bs4 import BeautifulSoup as bs

#for header analysis
def header(target):
	print("\n Printing headers...")
	try:
	        res = requests.get(target)

	        if res.status_code == 200:
	                print("response: ", res.status_code)
	                print("Headers:", "\nserver: ", res.headers.get('server'), "\nContent-Type: ", res.headers.get('content-type'), "\nX-Frame-Option: ", res.headers.get('X-frame-option'), "\nX-XSS-Protection: ", res.headers.get('x-xss-protection'), "\nContent-Security_policy: ", res.headers.get('content-security-policy'), "\nCross-Orgin-Resource-Policy: ", res.headers.get('cross-orgin-resource-policy'), "\nX-Content-Type-Options: ", res.headers.get('x-content-type-options'))
	                print("\n\nCookies:", res.cookies)

	except Exception as e:
	        print(e)

#to get input fields for input validation
def validation(target):
	print("\n Printing <form>....")
	try:
		con = requests.get(target)
		if con.status_code == 200:
			resp = con.text
			rep = bs(resp, "html.parser")
			forms = rep.find_all('form')
			for form in forms:
				print("\n\n", form.prettify())
		else:
			print(con.status_code)

	except Exception as e:
		print(e)
#get links
def crawl(target):
	custom = input("Enter user-agent: ")
	header = {"user-agent": custom}
	print("\n Getting Links")
	try:
		con = requests.get(target, headers=header)
		if con.status_code == 200:
			resp = con.text
			res = bs(resp, 'html.parser')
			links = res.find_all('a')
			for link in links:
				print(link)
		else:
			print(con.status_code)
	except Exception as e:
		print(e)


print("""
\t\t\t\tWELCOME
Select Option
1) Header analysis
2) form Extraction
3) Web Crawler
""")
option = input(">>> ")
site = input("Enter URL(https://www.target.com): ")

if option == '1':
	header(site)
elif option == '2':
	validation(site)
elif option == '3':
	crawl(site)
else:
	print("invaild option")
