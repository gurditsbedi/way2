#!/usr/bin/python

import urllib2
import cookielib
import sys
import argparse


def fetchInputs():
    '''To catch the neccesary data from the command line inputs '''
    format_class = lambda prog: argparse.HelpFormatter(prog,
                                                       max_help_position=55)
    parser = argparse.ArgumentParser(description='Command line tool to send '
                                     'send via way2 website.',
                                     formatter_class=format_class)
    parser.add_argument('-u',
                        help='Registered Mobile Number',
                        required='True',
                        metavar='Mobile-Number',
                        )

    parser.add_argument('-p',
                        help='Password',
                        metavar='Password',
                        required='True')

    parser.add_argument('-t',
                        help='Receiver\'s Mobile Number',
                        metavar='To',
                        required='True')

    parser.add_argument('-m',
                        help='Message to be send.',
                        metavar='Message',
                        required='True')

    results = parser.parse_args()

    return results


def sendSMS():
    ''' Sends the SMS'''

    inputs = fetchInputs()

    uname = inputs.u
    passwd = inputs.p
    to = inputs.t
    # Limiting the size of the message to 140 Chars
    message = inputs.m[0:139]
    # Transforming message to be encoded into the URL
    message = "+".join(message.split(' '))

    # Logging into the SMS Site
    url = 'http://site24.way2sms.com/Login1.action?'
    data = 'username=' + uname + '&password=' + passwd + '&Submit=Sign+in'

    # For Cookies:
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    # Adding Header detail:
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/37.0.2062.120 Safari/537.36')]

    try:
        usock = opener.open(url, data)
    except IOError:
        print "Error while logging in."
        sys.exit(1)

    # Parsing of token
    jession_id = str(cj).split('~')[1].split(' ')[0]

    # Creating the url required to send the message
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token=' + jession_id + '&mobile=' + to \
        + '&message=' + message + '&msgLen=136'
    opener.addheaders = [
        ('Referer', 'http://site25.way2sms.com/sendSMS?Token=' + jession_id)]

    # Sending the message
    try:
        sms_sent_page = opener.open(send_sms_url, send_sms_data)
    except IOError:
        print "Error while sending message"
        sys.exit(1)

    print "SMS has been sent."


if __name__ == '__main__':
    sendSMS()
