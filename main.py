#!/usr/local/bin/python
# coding: latin-1

from requestUrl import getContent

def main():
  saisie = raw_input("URL à requéter : ")
  result = getContent(url=saisie)

  print(result)

if __name__ == "__main__":
  main()