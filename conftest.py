import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='ru, en',  # или default=None,
        help='Language'
    )