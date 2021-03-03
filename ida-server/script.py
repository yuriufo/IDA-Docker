# -*- coding: utf-8 -*-

import os, json, traceback
import idc, idautils, ida_auto, idaapi, ida_nalt


features = {"EA": []}


def analysis():
    for ea in idautils.Functions():
        flags = idc.get_func_flags(ea)
        # 筛选 THUNK (跳转) or 典型库函数
        if flags & idc.FUNC_LIB or flags & idc.FUNC_THUNK:
            continue
        features['EA'].append(f"{ea:X}")


def main():
    analysis()


if __name__ == "__main__":
    # 运行脚本逻辑前等待自动分析完成
    ida_auto.auto_wait()
    binary_name = ida_nalt.get_root_filename().split('.')[0]
    path = ida_nalt.get_input_file_path()[:-len(ida_nalt.get_root_filename())]
    outputPath = os.path.join(path, 'result.json')
    try:
        main()
        # 输出特征为json
        with open(outputPath, "w") as f:
            f.write(json.dumps(features)) # , indent=2
    except Exception as e:
        # 发生异常
        traceback.print_exc(file=open(outputPath, "error"))
    idc.qexit(0)
