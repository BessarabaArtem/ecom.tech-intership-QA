from playwright.sync_api import sync_playwright
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Открываем сайт
    page.goto("https://kuper.ru")
    
    # Ждем пока загрузится сайт, а то кнопки не нажимаются
    time.sleep(5) 

    # Ищем кнопки. Я скопировал XPath из браузера
    delivery_btn = page.locator('//*[@id="root"]/div/div[1]/header/div/div/div/button[1]')
    pickup_btn = page.locator('text=Самовывоз')

    # Кликаем на самовывоз
    pickup_btn.click()
    
    # Ждем переключения
    time.sleep(2)

    # Проверяем атрибут aria-selected
    # Должно стать true у кнопки самовывоза
    status = pickup_btn.get_attribute("aria-selected")
    
    # Проверка
    if status == True:
        print("Тест прошел! Кнопка выбрана.")
    else:
        print("Тест упал. Атрибут равен:", status)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)

# P.S. Вроде разобрался с плэйрайтом, но все равно вылетают ошибки и не могу понять почему(((