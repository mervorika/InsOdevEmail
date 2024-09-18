import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()

HOME_PAGE_LOCATOR = "https://inshoppingcart.inone.useinsider.com/"
HomePageExpectedTitle = "Inone - Login - Insider Inone"

driver.get(HOME_PAGE_LOCATOR)
time.sleep(2)
assert HomePageExpectedTitle == driver.title
print("INFO: inshoppingcart anasayfası başarıyla açıldı.")


SIGN_IN_EMAIL_LOCATOR = '//input[@id="email"]'
emailInput = driver.find_element(by=By.XPATH, value = SIGN_IN_EMAIL_LOCATOR)
emailInput.send_keys("EMAIL")

SIGN_IN_PASSWORD_LOCATOR = '//input[@id="password"]'
passwordInput = driver.find_element(by=By.XPATH, value = SIGN_IN_PASSWORD_LOCATOR)
passwordInput.send_keys("PASSWORD")

SIGN_IN_SUBMIT = '//button[@id="login-button"]'
submitButton = driver.find_element(by=By.XPATH, value = SIGN_IN_SUBMIT)
submitButton.click()

time.sleep(2)


EMAIL_PAGE_LOCATOR = "https://inshoppingcart.inone.useinsider.com/email"

driver.get(EMAIL_PAGE_LOCATOR)
time.sleep(2)

CREATE_EMAIL_CAMP = '//button[@id="create"]'
createButton = driver.find_element(by=By.XPATH, value = CREATE_EMAIL_CAMP)
createButton.click()

time.sleep(3)
campaignName = "mbemailtest"

CAMPAIGN_NAME_LOCATOR = '//input[@id="campaign-name"]'
campName = driver.find_element(by=By.XPATH, value = CAMPAIGN_NAME_LOCATOR)
campName.send_keys(campaignName)


CREATE_BUTTON = '//button[@id="accept"]'
createButton = driver.find_element(by=By.XPATH, value = CREATE_BUTTON)
createButton.click()

time.sleep(10)

INCLUDE_RECIPIENT = '//div[@id="include-recipient-list"]'
includeRecipients = driver.find_element(by=By.XPATH, value = INCLUDE_RECIPIENT)
includeRecipients.click()

INCLUDE_RECIPIENT_SEARCH = '//input[@id="include-recipient-list-search"]'
includeRecipientsSearch = driver.find_element(by=By.XPATH, value = INCLUDE_RECIPIENT_SEARCH)
includeRecipientsSearch.send_keys("merve")

SELECT_CONTACT_LIST = '//label[contains(@for, "mervetest")]'
selectContactList = driver.find_element(by=By.XPATH, value = SELECT_CONTACT_LIST)
selectContactList.click()

ATTRIBUTES_LOCATOR = '//a[contains(@class, "qa-attributes")]'
attributesButton = driver.find_element(by=By.XPATH, value = ATTRIBUTES_LOCATOR)
attributesButton.click()

SEGMENT_SELECTOR = '//button[@id="conditionList0"]'
ruleSelector = driver.find_element(by=By.XPATH, value = SEGMENT_SELECTOR)
ruleSelector.click()

EMAIL_ADDRESS_SEGMENT_LOCATOR = '//a[contains(@class, "conditionList0-email-address")]'
emailAddressSegment = driver.find_element(by=By.XPATH, value = EMAIL_ADDRESS_SEGMENT_LOCATOR)
emailAddressSegment.click()

VALUE_BUTTON = '//div[contains(@class, "segment-content-wrapper")]//div[contains(@class, "in-dropdown-wrapper__input")]'
valueButton = driver.find_element(by=By.XPATH, value = VALUE_BUTTON)
valueButton.click()

SEARCH_VALUE = '//div[contains(@class, "segment-content-wrapper")]//div[contains(@class, "in-dropdown-wrapper__input")]//following-sibling::div//input[@name="drop-down-search"]'
searchValue = driver.find_element(by=By.XPATH, value = SEARCH_VALUE)
searchValue.send_keys("insqat@gmail.com")

time.sleep(10)

MY_EMAIL_BUTTON = '//label[@for="insqat@gmail.com"]'
myEmailButton = driver.find_element(by=By.XPATH, value = MY_EMAIL_BUTTON)
myEmailButton.click()


SAVE_NEXT_BUTTON = '//button[@id="save-and-next"]'
saveNextButton = driver.find_element(by=By.XPATH, value = SAVE_NEXT_BUTTON)
saveNextButton.click()

time.sleep(14)


SUBJECT = '//div[@id="subject-0-attribute"]'
subject = driver.find_element(by=By.XPATH, value = SUBJECT)
subject.send_keys("asd")


CHOOSE_TEMP_BUTTON = '//a[@id="choose-template-btn"]'
tempButton = driver.find_element(by=By.XPATH, value = CHOOSE_TEMP_BUTTON)
tempButton.click()

time.sleep(10)

CUSTOM_SELECTOR = '//button[@id="qa-custom"]'
customSelector = driver.find_element(by=By.XPATH, value = CUSTOM_SELECTOR)
customSelector.click()

time.sleep(4)

TEMPLATE = '//div[contains(@class, "template-selection__template-boxes")]/child::div[1]'
template = driver.find_element(by=By.XPATH, value = TEMPLATE)
template.click()

time.sleep(4)

APPLY_TEMPLATE = '//div[@id="preview-template-modal"]//button[@id="accept"]'
applyTemplate = driver.find_element(by=By.XPATH, value = APPLY_TEMPLATE)
applyTemplate.click()

time.sleep(16)

SAVE_NEXT_BUTTON = '//button[@id="save-and-next"]'
saveNextButton = driver.find_element(by=By.XPATH, value = SAVE_NEXT_BUTTON)
saveNextButton.click()

time.sleep(8)

SAVE_NEXT_BUTTON = '//button[@id="save-and-next"]'
saveNextButton = driver.find_element(by=By.XPATH, value = SAVE_NEXT_BUTTON)
saveNextButton.click()

time.sleep(8)

SEND_NOW = '//label[@for="Send Now"]'
sendNow = driver.find_element(by=By.XPATH, value = SEND_NOW)
sendNow.click()

time.sleep(4)

SAVE_NEXT_BUTTON = '//button[@id="save-and-next"]'
saveNextButton = driver.find_element(by=By.XPATH, value = SAVE_NEXT_BUTTON)
saveNextButton.click()

time.sleep(10)

SEND_BUTTON = '//button[@id="accept"]'
sendButton = driver.find_element(by=By.XPATH, value = SEND_BUTTON)
sendButton.click()

time.sleep(6)

ASSERT_SEND_TIME = '//div[@data-information="'+campaignName+'"]/../../../td[contains(@class,"start-date")]//span'
assertSendTime = driver.find_element(by=By.XPATH, value=ASSERT_SEND_TIME)
assert assertSendTime.text != " "
print("INFO: Email başarıyla gönderildi!")

time.sleep(4)
