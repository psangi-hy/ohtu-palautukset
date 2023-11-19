*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
	Set Username  kalle
	Set Register Password  kalle123
	Submit Register Credentials
	Register Should Succeed

Register With Too Short Username And Valid Password
	Set Username  ka
	Set Register Password  kalle123
	Submit Register Credentials
	Register Should Fail With Message  The username must be at least 3 characters long

Register With Valid Username And Invalid Password
	Set Username  kalle
	Set Register Password  kallekalle
	Submit Register Credentials
	Register Should Fail With Message  The password may not consist only of letters

Register With Nonmatching Password And Password Confirmation
	Set Username  kalle
	Input Password  password  kalle123
	Input Password  password_confirmation  kalle456
	Submit Register Credentials
	Register Should Fail With Message  The password and password confirmation fields do not match

Login After Successful Registration
	Register  kalle  kalle123
	Go To Login Page
	Set Username  kalle
	Set Password  kalle123
	Submit Credentials
	Login Should Succeed

Login After Failed Registration
	Register  kalle  kalle
	Go To Login Page
	Set Username  kalle
	Set Password  kalle
	Submit Credentials
	Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
	Welcome Page Should Be Open

Register Should Fail With Message
	[Arguments]  ${message}
	Register Page Should Be Open
	Page Should Contain  ${message}

Submit Register Credentials
	Click Button  Register

Set Register Password
	[Arguments]  ${password}
	Input Password  password  ${password}
	Input Password  password_confirmation  ${password}

Register
	[Arguments]  ${username}  ${password}
	Go To Register Page
	Set Username  ${username}
	Set Register Password  ${password}
	Submit Register Credentials
