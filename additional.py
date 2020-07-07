#!/usr/bin/env python 
# encoding: utf-8 
# author: jeremyZ
# time: 2020/7/7 3:43 下午


def determine_recursive(v1, v2, count):
    if int(v1[-count]) > int(v2[-count]):
        result = 1
    elif int(v1[-count]) < int(v2[-count]):
        result = -1
    else:
        result = 0
    count -= 1
    if count:
        return result if result else determine_recursive(v1, v2, count)
    else:
        return result


def determine_version(version1, version2):
    version1_list = version1.split('.')
    version2_list = version2.split('.')
    if len(version1_list) > len(version2_list):
        count = len(version1_list)
        version2_list.extend(['0' for _ in range(len(version1_list)-len(version2_list))])
    elif len(version1_list) < len(version2_list):
        count = len(version2_list)
        version1_list.extend(['0' for _ in range(len(version2_list)-len(version1_list))])
    else:
        count = len(version1_list)

    return determine_recursive(version1_list, version2_list, count)


if __name__ == '__main__':
    version1 = input("请输入版本号1：")
    version2 = input("请输入版本号2：")
    result = determine_version(version1, version2)
    print(result)