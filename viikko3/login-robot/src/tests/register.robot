*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
	Input New Command
	Input Credentials  kalle  kalle123
	Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
	Input New Command
	Input Credentials  kalle  kalle123
	Input New Command
	Input Credentials  kalle  kalle321
	Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
	Input New Command
	Input Credentials  ka  kalle123
	Output Should Contain  The username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
	Input New Command
	Input Credentials  kalle1  kalle123
	Output Should Contain  The username may only contain the lower case letters a-z

Register With Valid Username And Too Short Password
	Input New Command
	Input Credentials  kalle  kalle12
	Output Should Contain  The password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
	Input New Command
	Input Credentials  kalle  kallekalle
	Output Should Contain  The password may not consist only of letters
