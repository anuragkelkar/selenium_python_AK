*** Settings ***

*** Variables ***
${MY_NAME}      Anurag
${MOBILE}      12345678

*** Test Cases ***
TC1
    Log To Console      message=Anurag Kelkar
    Log To Console    Welcome to robot session
    Log To Console    ${MY_NAME}

TC2
    Log To Console    ${MY_NAME}
    Log To Console    ${MOBILE}
    ${value}    Set Variable  45
    Log To Console    ${value}

TC3
    ${radius}   Set Variable    10
    ${area}     Evaluate    3.14*${radius}*${radius}
    Log To Console    ${area}
