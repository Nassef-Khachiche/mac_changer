#!/usr/bin/env python

import subprocess
import optparse


def getArguments():
    parser = optparse.OptionParser()
    parser.add_option("-n", "--network", dest="myNetwork", help="Network to change it's MAC address")
    parser.add_option("-a", "--address", dest="myAddress", help="New MAC address")
    return parser.parse_args()


def macChange(myNetwork, myAddress):
    print("[+] Changing network: " + myNetwork + " MAC address to " + myAddress)
    subprocess.call(["ifconfig", myNetwork, "down"])
    subprocess.call(["ifconfig", myNetwork, "hw", "ether", myAddress])
    subprocess.call(["ifconfig", myNetwork, "up"])


(options, args) = getArguments()
macChange(options.myNetwork, options.myAddress)
