import psutil
import platform
import wmi
import cpuinfo
import re


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
partitions = psutil.disk_partitions()

for partition in partitions:
    partition_usage = psutil.disk_usage(partition.mountpoint)

computer = wmi.WMI()
gpu_info = computer.Win32_VideoController()[0]


def Get_User_Info():
    OS = platform.system()
    version = platform.version()
    if OS == "Windows":
        if version < "10.0.22000":
            version = platform.release()
        else:
            version = "11"
        OS = f"Windows {version}"
    else:
        version = platform.release()  # Use platform.release() if OS is not Windows
        OS = f"{platform.system()}: {version}"

    # Get processor info
    processor_info = cpuinfo.get_cpu_info()['brand_raw']

    if "Intel" in processor_info:
        # Use regex to extract model
        match = re.match(r".*Intel\(R\) Core\(TM\) (i[0-9]+-[0-9a-zA-Z]+) .*", processor_info)
        if match:
            model = match.group(1)
        else:
            model = processor_info
        Processor = f"Intel Core {model}"
    else:
        Processor = processor_info

    Ram = get_size(psutil.virtual_memory().total)
    Rom = get_size(psutil.disk_usage("/").free)
    GPU = gpu_info.Name

    return OS, Processor, Ram, Rom, GPU