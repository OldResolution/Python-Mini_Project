import psutil
import platform
from datetime import datetime


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


swap = psutil.swap_memory()
svmem = psutil.virtual_memory()
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Device: {partition.device} ===")
    print(f"  Mountpoint: {partition.mountpoint}")
    print(f"  File system type: {partition.fstype}")
<<<<<<< Updated upstream
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue
    print(f"  Total Size: {get_size(partition_usage.total)}")
    print(f"  Used: {get_size(partition_usage.used)}")
    print(f"  Free: {get_size(partition_usage.free)}")
    print(f"  Percentage: {partition_usage.percent}%")
# get IO statistics since boot
disk_io = psutil.disk_io_counters()
print(f"Total read: {get_size(disk_io.read_bytes)}")
print(f"Total write: {get_size(disk_io.write_bytes)}")
=======
partition_usage = psutil.disk_usage(partition.mountpoint)
#graphics card for windows
computer = wmi.WMI()
gpu_info = computer.Win32_VideoController()[0]



def Get_User_Info():
    OS=platform.system()
    Proccesor=platform.processor()
    Ram=get_size(svmem.total)
    Rom=get_size(partition_usage.free)
    GPU=format(gpu_info.Name)

    return OS,Proccesor,Ram,Rom,GPU

>>>>>>> Stashed changes
