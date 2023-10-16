#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 3:
        print(f"{sys.argv[0]} <script> <target-binary>")
        sys.exit(1)

    scriptPath = sys.argv[1]
    targetPath = sys.argv[2]
    
    xorKey = 0x01

    with open(scriptPath, "rb") as sHandle:
        e_script = sHandle.read()
        with open(targetPath, "ab") as tHandle:
            for b in e_script:
                encryptedByte = b ^ xorKey
                tHandle.write(encryptedByte.to_bytes(1, byteorder="little"))
    

if __name__ == "__main__":
    main()
