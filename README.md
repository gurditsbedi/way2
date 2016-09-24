#way2

way2 is a command line tool(Unofficial) to send sms to any Indian Mobile Number.

#How-to

1. Register at way2sms. This will give you your account details. Only your registered mobile number and password is required.

2.  Install way2, git clone this repository or download the zip file of the repository. Upon completion. Go into the diretory and execute `python setup.py install`. This will install the way2 to command line tool.

3. To send a message type in the terminal 
`way2 -u Mobile-Number -p password -t receivers-number -m "your message"`
You get a confirmation message on success.

NOTE: There is limit on length of the sms according to the website which is 140 characters. The message you send is truncated to 140 chars and then it is send.

#Example

`way2 -u 987XXXXXXX -p password -t 801XXXXXXX -m "Hey, Where are you?"`

#Aliasing for shell users

If you are on a platform which has bash, zsh etc you would like to alias, because its too much typing for too less. Just and this following lines to your `~/.bash_aliases` in case of bash and you get `way2up` and `way2me ` commands.
```
alias way2up='way2 -u 987XXXXXXX -p password'
alias way2me='way2 -u 987XXXXXXX -p password -t 987XXXXXXX'
```


* `way2up`: In this one you have your mobile number and password stored just you have to provide reciever number and message.
* `way2me`: In this one you send message to yourself.

#Issues

* In India you are only allowed to send 100 sms per day per user, so the condition also applies here. This tool does not detect how many messages you have send on a day, so when you try send message after crossing this limit it will give positive reponse.

* When you cross the Indian daily sms limit, instead of giving negative respose will give positive response.

#Privacy

* The tool does not record an data such as mobile number, password or message. As the app is open-source you can review all of its code on GitHub to make sure it’s not logging or transmitting data somewhere.

#License

The MIT License (MIT)

Copyright (c) 2016 Gurdit Singh Bedi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
