import requests
from bs4 import BeautifulSoup


def get_usd_brl_rate():
    """
    Scrapes USD to BRL exchange rate from a public source.
    """
    url = "https://www.x-rates.com/calculator/?from=USD&to=BRL&amount=1"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        raise Exception("Failed to fetch FX rate page")

    soup = BeautifulSoup(response.text, "html.parser")

    # Find the rate element (site-specific selector)
    rate_tag = soup.find("span", class_="ccOutputRslt")
    if not rate_tag:
        raise Exception("Exchange rate not found in page")

    # Clean and convert to float
    rate_text = rate_tag.get_text().split(" ")[0]
    return float(rate_text.replace(",", ""))


if __name__ == "__main__":
    try:
        rate = get_usd_brl_rate()
        print(f"1 USD = {rate} BRL")
    except Exception as e:
        print("Error:", e)
