import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                 help="Choose language: 'ar' or 'ca' or 'cs' or 'da' or 'de' or 'en-gb' or 'el' or 'es' or 'fi' or 'fr' or 'it'")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language == "ar" or user_language == "ca" or user_language == "cs" or user_language =="da" or user_language == "de" or user_language == "en-gb" or user_language == "el" or user_language == "es" or user_language == "fi" or user_language == "fr" or user_language == "it":

        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be 'ar' or 'ca' or 'cs' or 'da' or 'de' or 'en-gb' or 'el' or 'es' or 'fi' or 'fr' or 'it'")
    yield browser
    print("\nquit browser..")
    browser.quit() 

    