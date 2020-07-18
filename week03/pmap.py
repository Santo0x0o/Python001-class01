# -*- coding: utf-8 -*-
# author: Santo
# update@ 2020/7/18

import argparse
import sys
import os
import subprocess
import ipaddress
import socket
from multiprocessing import Pool, Lock
from concurrent.futures import ThreadPoolExecutor as executor
import functools
import json
import time

# 因大家学习的操作系统版本不同，建立 tcp 连接的工具不限，可以使用 telnet、nc 或 Python 自带的 socket 套接字。
# -n：指定并发数量。
# -f ping：进行 ping 测试
# -f tcp：进行 tcp 端口开放、关闭测试。
# -ip：连续 IP 地址支持 192.168.0.1-192.168.0.100 写法。
# -p: tcp测试目标端口，支持0-1024; 80,443,139;
# -w：扫描结果进行保存。


class UserInputError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo


# print_lock =Lock()

def validate_port(p):
    if 0 < p < 65536:
        return(p)
    else:
        raise UserInputError(f'ValueError: {p} does not appear to be a port')


def validate_ip(ip):
    try:
        valid_ipv4 = ipaddress.IPv4Address(ip)
        return(valid_ipv4)
    except ValueError:
        raise UserInputError(
            f'ValueError: {ip} does not appear to be an IP address')


def generate_ip_list(s, e):
    for ips in ipaddress.summarize_address_range(ipaddress.IPv4Address(s), ipaddress.IPv4Address(e)):
        # 生成ip网段
        # print(ips)
        yield from ips

# formalize the port


def port_init(args):
    args.p = (None if args.f == 'ping' else args.p)
    port_list = []
    if args.f == 'tcp' and args.p is None:
        print('usage: pmap.py [-h] -f {ping,tcp} -ip IP [-p P] [-n N] [-w W]')
        raise UserInputError(
            'pmap.py: error: the following argument -p is mandatory for tcp test.')
    elif args.f == 'tcp' and args.p == []:
        args.p = ['1-1024']
        port_list = [p for p in range(1, 1025)]
    elif args.f == 'tcp' and args.p != []:
        for p in args.p:
            port_list.append(validate_port(p))
    return port_list

# formalize the ip addresss


def ip_init(args):
    ip_list = []
    if '-' in args.ip[0] and len(args.ip) > 1:
        # print('usage: pmap.py [-h] -f {ping,tcp} -ip IP [-p P] [-n N] [-w W]')
        raise UserInputError(
            'pmap.py: error: input the following argument -ip value in wrong format.')
    elif '-' in args.ip[0] and len(args.ip) == 1:
        ip_s, ip_e = args.ip[0].split('-')
        ip_list = list(generate_ip_list(ip_s, ip_e))
    else:
        for ip in args.ip:
            ip_list.append(validate_ip(ip))
    return ip_list


def ping_func(ip):
    # print('start ping')
    result = subprocess.run(f'ping {ip} -n 3', stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        # with print_lock:
        print(f'ping {ip} successed.')
        return {str(ip): 1}
    else:
        # with print_lock:
        print(f'ping {ip} failed.')
        return {str(ip): 0}


def tcp_func(ip, port):
    t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    t.settimeout(3)
    try:
        if t.connect_ex((ip, port)) == None:
            print(f'{port} of {ip} is Up')
            return {str(ip)+"_"+str(port): 1}
    except ConnectionRefusedError:
        print(f'{port} of {ip} is Down')
        return {str(ip)+"_"+str(port): 0}


def pmap(args):
    st = time.time()
    n = 2 if args.n == None else args.n
    host = ip_init(args)
    port = port_init(args)
    output_dict = {}
    output = []

    if args.m == 'proc':
        if args.f == 'ping':
            pool = Pool(n)
            output = pool.map(ping_func, host)
            pool.close()
            pool.join()

        if args.f == 'tcp':
            for i in host:
                pool = Pool(n)
                output += pool.map(functools.partial(tcp_func, str(i)), port)
                pool.close()
                pool.join()
    if args.m == 'thread':
        with executor(n) as pool:
            if args.f == 'ping':
                output = pool.map(ping_func, host)

            if args.f == 'tcp':
                for i in host:
                    output += pool.map(functools.partial(tcp_func,
                                                         str(i)), port)
    if args.w:
        for l in output:
            output_dict.update(l)
        ouput_json = json.dumps(output_dict, indent=4, sort_keys=True)
        t = time.strftime('%Y%m%d%H%M%S', time.localtime())
        with open('./'+args.f+'_test_result_'+t+'.json', 'wt') as f:
            f.write(ouput_json)
        print('output saved in json file:./'+args.f+'_test_result_'+t+'.json')
    et = time.time()
    if args.v:
        print(f'Scanning spent {str(round(et-st,3))} s')


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(
        description='-'*25+'Help info of pmap tool'+'-'*25)
    argparser.add_argument('-f', type=str, required=True, choices=[
                           'ping', 'tcp'], help='"ping" for ping test; "tcp" for port connectinity test.')
    argparser.add_argument('-ip', type=str, nargs='+', required=True,
                           help='ipV4 address, support single or patch in format "192.168.0.1-192.168.0.100"; "192.168.0.1 192.168.0.3".')
    argparser.add_argument('-p', type=int, nargs='*',
                           help='port mandatory for tcp test, support single or patch in format "1-1024"(default); "80 443" .')
    argparser.add_argument('-m', type=str, choices=['proc', 'thread'],
                           required=True, help='select to run by multiprocess or multithread.')
    argparser.add_argument(
        '-n', type=int, choices=[2, 4, 8], help='Num of multi job.')
    argparser.add_argument('-w', action='store_true',
                           help='Save the scan result to current folder.')
    argparser.add_argument('-v', action='store_true',
                           help='Show the time spending for scan test.')
    args = argparser.parse_args()
    pmap(args)
