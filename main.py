#!/usr/bin/env python3
from A_MIA_R3_Core.Face_Process import Face_Process


def main():
    fp=Face_Process("koizumi_7_30.mp4")
    fp.get_videoinfo()
    print("Hello")


if __name__ == '__main__':
    main()
