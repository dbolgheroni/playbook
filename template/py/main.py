#!/usr/bin/env python3

from pb import fake_payload

@fake_payload(max=2.0)
def payload():
    pass

def main():
    payload()

if __name__ == '__main__':
    main()
