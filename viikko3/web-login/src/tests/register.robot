*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
	Set Username  kalle
	Set Password  kalle123
	Submit Credentials
	Register Should Succeed

Register With Too Short Username And Valid Password
	Set Username  ka
	Set Password  kalle123
	Submit Credentials
	Register Should Fail With Message  The username must be at least 3 characters long

Register With Valid Username And Invalid Password
	Set Username  kalle
	Set Password  kallekalle
	Submit Credentials
	Register Should Fail With Message  The password may not consist only of letters

Register With Nonmatching Password And Password Confirmation
	Set Username  kalle
	Input Password  password  kalle123
	Input Password  password_confirmation  kalle456
	Submit Credentials
	Register Should Fail With Message  The password and password confirmation fields do not match

*** Keywords ***
Register Should Succeed
	Welcome Page Should Be Open

Register Should Fail With Message
	[Arguments]  ${message}
	Register Page Should Be Open
	Page Should Contain  ${message}

Submit Credentials
	Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
	[Arguments]  ${password}
	Input Password  password  ${password}
	Input Password  password_confirmation  ${password}
