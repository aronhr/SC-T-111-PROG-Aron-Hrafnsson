from splinter import Browser

with Browser('chrome') as browser:
    # Visit URL
    url = "http://www.bing.com"
    browser.visit(url)

    # fill the query form with our search term
    browser.fill('sb_form_q', 'mastro35 twitter')

    # find the search button on the page and click it
    button = browser.find_by_id('sb_form_go')
    button.click()
