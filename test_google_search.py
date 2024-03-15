from selene import browser, be, have


def test_google_search(setting_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_empty_result(setting_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('&%^&^(%&%(7khjkhkjhkhkhkkj#####').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
