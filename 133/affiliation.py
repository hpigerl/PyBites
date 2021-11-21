def generate_affiliation_link(url: str):
    asin_start = url.find("dp/") + 3
    asin_end = url.find("/", asin_start)
    if asin_end == -1:
        asin = url[asin_start:]
    else:
        asin = url[asin_start:asin_end]
    affil_link = "http://www.amazon.com/dp/" + asin + "/?tag=pyb0f-20"
    return affil_link
