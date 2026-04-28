from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

def search_and_add(page, query):
    page.goto('https://www.amazon.in/')
    page.wait_for_load_state("domcontentloaded")

    try:
        page.get_by_role("button", name="Continue shopping").click(timeout=5000)
    except PlaywrightTimeoutError:
        print("No Pop up to accept")

    page.fill("#twotabsearchtextbox", query)
    page.keyboard.press("Enter")

    page.wait_for_selector("div.s-main-slot .s-result-item.s-asin")

    item = page.locator("div.s-main-slot .s-result-item.s-asin")
    new_page = None
    for i in range(item.count()):
        current = item.nth(i)
        if current.locator("text=Sponsored").count() > 0:
            continue

        link = current.locator("h2 a").first
        if link.count() == 0:
            continue
        try:
            with page.context.expect_page(timeout=3000) as new_page_info:
                link.scroll_into_view_if_needed()
                link.click(force=True)
            new_page = new_page_info.value
            new_page.wait_for_load_state("domcontentloaded")
            break
        except Exception:
            page.wait_for_load_state("domcontentloaded")
            new_page = page
            break

    if not new_page:
        print("No product could be opened")
        return

    price = None
    for sel in [".a-price .a-offscreen", ".priceToPay .a-offscreen"]:
        loc = new_page.locator(sel)
        if loc.count() > 0:
            price = loc.first.inner_text()
            break

    if price:
        print(f"{query} Price:", price)
    else:
        print("Price not found")

    if new_page.locator("#add-to-cart-button").count() > 0:
        new_page.click("#add-to-cart-button")
        try:
            new_page.wait_for_selector("#NATC-SMART-WAGC-MODAL, #huc-v2-order-row-confirm-text", timeout=5000)
            print("Added to cart successfully")
        except PlaywrightTimeoutError:
            print("Cart confirmation selector not found, may still have worked")
    else:
        print("Add to Cart not available")

def test_iphone(page):
    search_and_add(page, "iphone")

def test_samsung(page):
    search_and_add(page, "samsung galaxy")