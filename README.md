📊 Explanation of the Script
Fetch Web Page:

requests.get() fetches the Oxylabs product page.
A User-Agent header prevents anti-bot mechanisms.
Parse HTML Content:

BeautifulSoup parses the HTML response.
Extracts:
Product Name (h3.product-name)
Description (p.product-description)
Price (span.product-price)
Availability (span.product-availability)
Store Data:

Data is collected in a Python list.
Save to CSV:

Data is exported into a CSV file using pandas.
