#!/usr/bin/env python3

import ipaddress
from os import system
import re
import sys
from colorama import Fore, Back, Style

inv_file = 'inventory.yml'
XCC = Fore.BLACK + Back.GREEN
XCX = Style.RESET_ALL + Fore.GREEN


def clean():
    print(Style.RESET_ALL)
    system('clear')
    print(XCX)
class newserver:
    cip = '10.100.10.1'
    nip = ''
    dns = ''
    fqdns =  ''
    olddns = ''
    gway = ''
    bcast = ''
    nwork = ''
    nmask= '24'

def validateip(ip_string):
    try:
        ip_object = ipaddress.ip_address(ip_string)
        checkb = 0
    except ValueError:
        checkb = 1
    return(checkb, ip_string)

def validatecrd(data) :
    if data > 0 and data <31:
        checkb = 0
        newserver.nmask = data
        return(checkb, data, newserver.nmask)
    else:
        checkb = 1
        newserver.nmask = '24'
        return(checkb, data, newserver.nmask)
    print(type(data))
    cdr_string = int(data)
    print(type(cdr_string))
    exit()

def validatedns(srt_string):
    ini_str = srt_string.lower()
    a="abcdefghijklmnopqrstuvwxyz-"
    c=0
    for i in ini_str:
        if i in a:
            c+=1
    if(c==len(ini_str)):
        checkb = 0
    else:
        checkb = 1
        print("Hibas tartalma a volt a DNS nevnek! Kérem jót adjál meg.")
    return(checkb)

def readdatas():
    clean()
    checkb = 1
    print('A DNS nev nem lehet hosszabb mint 255 karakter. Ha hosszabb 255 folotti resz eldobasra kerul.')
    print('Kizarolag ekezet mentes karakterek es a - hasznalhato.')
    while (checkb != 0) :
        newserver.dns = input("A szerver DNS neve: ")
        newserver.dns = newserver.dns[: 255]
        checkb = validatedns(newserver.dns)
    newserver.fqdns = newserver.dns + "." + "kesz.hu"
    newserver.olddns = newserver.dns[: 14].upper()

    print('\nA szerver halozati adatainak megadása:')
    print('+---------------------------------------')
    checkb = 1
    while (checkb != 0) :
        indata = input("A szerver jelenlegi IP cime (" + newserver.cip + "): ")
        if indata == '':
            indata = newserver.cip
            checkb = 0
        if indata != '':    
            checkb, newserver.cip = validateip(indata)

    checkb = 1
    while (checkb != 0) :
        indata = input("A szerver új IP cime: ")
        checkb, newserver.nip = validateip(indata)
        TEMP = newserver.nip.split(".")
        TEMP[3] = '0'
        newserver.nwork = TEMP[0] + "." + TEMP[1] + "." + TEMP[2] + "." + TEMP[3]
        TEMP[3] = '255'
        newserver.bcast = TEMP[0] + "." + TEMP[1] + "." + TEMP[2] + "." + TEMP[3]
        TEMP[3] = '254'
        newserver.gway = TEMP[0] + "." + TEMP[1] + "." + TEMP[2] + "." + TEMP[3]

    checkb = 1
    while (checkb != 0) :
        indata = input("A halozati mask (" + str(newserver.nmask) + "): ")
        indata = int(indata)
        if indata == '':
            indata = newserver.nmask
            checkb = 0
        if indata != '':    
            checkb, newserver.nmask, newserver.nmask = validatecrd(indata)

    checkb = 1
    while (checkb != 0) :
        indata = input("A halozat (" + newserver.nwork + "): ")
        if indata == '':
            indata = newserver.nwork
            checkb = 0
        if indata != '':
            checkb, newserver.nwork = validateip(indata)

    checkb = 1
    while (checkb != 0) :
        indata = input("A halozat broadcast cime (" + newserver.bcast + "): ")
        if indata == '':
            indata = newserver.bcast
            checkb = 0
        if indata != '':    
            checkb, newserver.bcast = validateip(indata)

    checkb = 1
    while (checkb != 0) :
        indata = input("A halozat gateway cime (" + newserver.gway + "): ")
        if indata == '':
            indata = newserver.gway
            checkb = 0
        if indata != '':    
            checkb, newserver.gway = validateip(indata)

def checkdatas():
    checkb = 1
    while (checkb != 0):
        clean()
        print('Az alábbi adatoknak megfelelően kerül beállításra a SZERVER. Kérem ellenőrizd, hogy az adatok megfelelőek.\n') 
        print('A szerver jelenlegi IP cime:\t' + newserver.cip)
        print('Szerver adatai:')
        print('---------------')
        print('\t-   IP cime:  ' + XCC + newserver.nip + XCX)
        print('\t-   netmask:  ' + XCC +  str(newserver.nmask) + XCX)
        print('\t- broadcast:  ' + XCC +  newserver.bcast + XCX)
        print('\t-   gateway:  ' + XCC +  newserver.gway + XCX)
        print('\t-   network:  ' + XCC +  newserver.nwork + XCX)
        print('\t-  DNS neve:  ' + XCC +  newserver.dns + XCX)
        print('\t- FQND neve:  ' + XCC +  newserver.fqdns + XCX)
        print('\t-(OLD) neve:  ' + XCC +  newserver.olddns + XCX)

        A = input('Megfelelően az adatok (Y/n):')
        if A == '':
            checkb = 0
        if A == 'Y':
            checkb = 0
        if A == 'N':
            checkb = 1
    return(checkb)

def inventory_write():
    f = open(inv_file, "w")
    f.write('all:\n')
    f.write('  children:\n')
    f.write('    host:\n')
    f.write('      osszes:\n')
    f.write('        new-server:\n')
    f.write('          ansible_host: ' + newserver.cip + '\n')
    f.write('    var:\n')
    f.write('      file_nev: osszes\n')
    f.write('      ansible_user: ansible\n')
    f.write('      ntp-server: ns1.pcsaba.comcast.lan\n')
    f.write('      ntp-servers:\n')
    f.write('      - ns2.pcsaba.comcast.lan\n')
    f.close()

def interfaces_write():
    f = open('interfaces', 'w')
    f.write('auto lo\n')
    f.write('iface lo inet loopback\n')
    f.write('\n\n')
    f.write('alow-hotplug ens18\n')
    f.write("iface ens18 inet static\n")
    f.write("  address " + newserver.nip + '\n')
    f.write("  network " + newserver.nwork + '\n')
    f.write("  netmask " + str(newserver.nmask) + '\n')
    f.write("  gateway " + newserver.gway + '\n')
    f.write("  broadcast " + newserver.bcast + '\n')
    f.close()

def hosts_write():
    f = open('hosts', 'a')
    f.write(newserver.nip + '  ' + newserver.dns + '  ' + newserver.fqdns + '\n')
    f.close()

def files_write() :
    inventory_write()
    interfaces_write()
    hosts_write()

def main():
    readdatas()
    checkdatas()
    files_write()
main()


