*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      https://www.facebook.com/
${BROWSER}        Chrome

*** Test Cases ***

TC Login
    Open Browser    browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait  20s
    Go To    url=${LOGIN URL}
    Input Text    locator=id=email    text=ak9234@gmail.com
    Input Password    locator=id=pass    password=pass
    Click Element    locator=name=login
    [Teardown]    Close Browser

