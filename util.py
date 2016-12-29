import argparse
import requests
import socket


def setup_args():
    parser = argparse.ArgumentParser(description='control with applescripts')
    parser.add_argument('phone', metavar='phone', type=str,
                        help='phone # that receives ip')
    parser.add_argument('--public', action='store_true',
                        help='whether to make server public')
    return parser


def text_ip(phone):
    ip = socket.gethostbyname(socket.gethostname())
    url = '  http://' + ip + ':5000/'
    payload = {'number': phone, 'message': url}
    print requests.post('http://textbelt.com/text', data=payload)
