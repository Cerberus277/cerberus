import os, sys, ctypes

if sys.version[0:3] != "3.9":
  sys.exit("[+]  python kamu tidak support di versi 3.9, versi python kamu sekarang : "+sys.version[0:3])

run = None

try:
  run = __import__("cerberus")
except Exception as s:
  sys.exit("[!] Error: %s"%(s))

if str(run).startswith("<module ") == False:
  sys.exit("[*] kesalahan pastikan kamu menginstall semua module di -> https://github.com/Cerberus277/cerberus")

if __name__ == "__main__":
  try:
    run()
  except Exception as s:
    exit("[!] Error: %s"%(s)))

