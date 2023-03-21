from playwright.sync_api import sync_playwright
import time, save_data as sd, re

global end, data
end = 9999
data = {}

def run(playwright, uid):
    webkit = playwright.webkit
    browser = webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    

    for start in range(end):
        try:
            page.goto(f"https://steamcommunity.com/id/{uid}/friends/")
            
            page.locator(".friend_block_v2 > a").nth(start).click()
            time.sleep(1)

            url = page.url
            inventario_amigo = url + '/inventory/'
            page.goto(inventario_amigo)

            nome_amigo = page.locator(".persona_name_text_content").text_content()
            nome_amigo = re.sub('\s+', '', nome_amigo)

            data["nome_amigo"] = nome_amigo
            data["uid"] = uid
            itens(page)

            sd.render_html(data)

        except:
            print("fudeu")
            break


    # page.screenshot(path="screenshot.png")
    browser.close()

def itens(page):
    cont = 0
    try:
        page.locator("#inventory_link_730").click()
        total = page.locator(".itemHolder > .app730 ").count()

        for i in range(total):
            page.locator(".itemHolder > .app730 ").nth(i).click()

            if i == 0:
                variabel = page.locator("#iteminfo1_item_name").text_content()
                # print(variabel)
                data["item" + str(i)] = variabel

            else:
                variabel = page.locator("#iteminfo1_item_name").text_content()
                # print(page.locator("#iteminfo0_item_name").text_content())
                data["item" + str(i)] = variabel
            
            cont += 1
            if cont == 25:
                cont = 0
                page.locator("#pagebtn_next").click()
                time.sleep(1)

    except:
        print("fudeo")


with sync_playwright() as playwright:
    uid = str(input("Insira seu ID Steam: "))
    run(playwright, uid)