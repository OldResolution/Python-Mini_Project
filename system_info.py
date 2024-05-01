import psutil
import platform
from datetime import datetime
import wmi

value = [["Memory"],
        ['Graphics Card'],
        ['CPU'],
        ['File Size'],
        ['OS']]
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


svmem = psutil.virtual_memory()

swap = psutil.swap_memory()

partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Device: {partition.device} ===")
    print(f"  Mountpoint: {partition.mountpoint}")
    print(f"  File system type: {partition.fstype}")
partition_usage = psutil.disk_usage(partition.mountpoint)

computer = wmi.WMI()
gpu_info = computer.Win32_VideoController()[0]

def Get_User_Info():
    OS=platform.system()
    Proccesor=platform.processor()
    Ram=get_size(svmem.total)
    Rom=get_size(partition_usage.free)
    GPU=format(gpu_info.Name)

    return OS, Proccesor, Ram, Rom, GPU


