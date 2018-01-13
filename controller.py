#! /usr/bin/env python3
import optparse


def main():
    p = optparse.OptionParser()
    p.add_option('--person', '-p', default="world", help="the test for the person!\nthe test for the person!\nthe test for the person!\n")
    p.add_option('--name', '-n', default="bob")
    options, arguments = p.parse_args()
    print("Hello {}".format(options.person))


if __name__ == '__main__':
    main()