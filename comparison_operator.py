import math
import psycopg2
from system_info import Get_User_Info  # Importing Get_User_Info function from system_info module

# Database connection information
Dbname = 'gamereq'
Username = 'postgres'
Password = 'oracle'
Hostname = 'localhost'
Port = '5432'

# Global variables for database connection and cursor
conn = None
cur = None

def cpu_gpu_rating(component, name):
    global conn, cur
    try:
        # Check if database connection exists, otherwise establish connection
        if not conn or conn.closed:
            connect_to_database()

        # Retrieve game hardware requirements
        cur.execute("SELECT component_rating FROM sys_components WHERE component_type = %s AND component_name = %s ", (component, name,))
        rating = cur.fetchall()
        return rating
    except psycopg2.Error as e:
        print(f"Error retrieving game hardware information: {e}")
        return None

# Function to establish connection to the PostgreSQL database
def connect_to_database():
    global conn, cur
    try:
        # Connect to the database
        conn = psycopg2.connect(
            dbname=Dbname,
            user=Username,
            password=Password,
            host=Hostname,
            port=Port
        )
        cur = conn.cursor()
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")

# Function to compare user's hardware information with game requirements
def Compare_minimum_info(gamename):
    # Retrieve user hardware information
    user_os, user_processor, user_ram, user_rom, user_gpu = Get_User_Info()
    user_CPU = cpu_gpu_rating("CPU", user_processor)
    user_GPU = cpu_gpu_rating("GPU", user_gpu)
    user_OS = cpu_gpu_rating("OS", user_os)
    # Retrieve game hardware requirements from the database
    game_hardware_info = game_mini_info(gamename)
    if game_hardware_info:
        game_CPU = cpu_gpu_rating("CPU", game_hardware_info['Processor'])
        game_GPU = cpu_gpu_rating("GPU", game_hardware_info['GPU'])
        game_OS = cpu_gpu_rating("OS", game_hardware_info['OS'])
    else:
        print("No game hardware information found.")
        return {}

    # Check compatibility for each component
    compatibility_status = {}

    # Compare OS
    if user_OS >= game_OS:
        print("OS is compatible")
        compatibility_status["OS"] = "Compatible"
    else:
        print("OS is not compatible")
        compatibility_status["OS"] = "Incompatible"

    # Compare RAM
    user_ram_float = math.ceil(float(user_ram[:-2]))
    game_ram_float = float(game_hardware_info['RAM'][:-2])
    if user_ram_float >= game_ram_float:
        print("RAM is compatible.")
        compatibility_status["RAM"] = "Compatible"
    else:
        print("RAM is incompatible.")
        compatibility_status["RAM"] = "Incompatible"

    # Compare Processor
    if user_CPU >= game_CPU:
        print("Processor is compatible.")
        compatibility_status["CPU"] = "Compatible"
    else:
        print("Processor is incompatible.")
        compatibility_status["CPU"] = "Incompatible"

    # Compare GPU
    if user_GPU >= game_GPU:
        print("GPU is compatible.")
        compatibility_status["GPU"] = "Compatible"
    else:
        print("GPU is incompatible.")
        compatibility_status["GPU"] = "Incompatible"

    # Compare ROM
    user_rom_float = math.ceil(float(user_rom[:-2]))
    game_rom_float = float(game_hardware_info['ROM'][:-2])
    if user_rom_float >= game_rom_float:
        print("ROM is compatible.")
        compatibility_status["ROM"] = "Compatible"
    else:
        print("ROM is incompatible.")
        compatibility_status["ROM"] = "Incompatible"

    # Determine final compatibility status
    all_components_compatible = all(status == "Compatible" for status in compatibility_status.values())
    if all_components_compatible:
        print(f"All components are compatible for {gamename}.")
    else:
        print(f"Not all components are compatible for {gamename}.")
    print(compatibility_status)
    return compatibility_status

# Function to retrieve game hardware requirements from the database
def game_mini_info(gamename):
    global conn, cur
    try:
        # Check if database connection exists, otherwise establish connection
        if not conn or conn.closed:
            connect_to_database()

        # Retrieve game hardware requirements
        cur.execute("SELECT * FROM game_requirements WHERE game_title = %s", (gamename,))
        game_hardware_info = cur.fetchone()

        if game_hardware_info:
            hardware_info = {
                'OS': game_hardware_info[2],
                'Processor': game_hardware_info[4],
                'RAM': game_hardware_info[6],
                'ROM': game_hardware_info[10],
                'GPU': game_hardware_info[8]
            }
            return hardware_info
        else:
            return None

    except psycopg2.Error as e:
        print(f"Error retrieving game hardware information: {e}")
        return None

# Close cursor and connection
def close_database_connection():
    global conn, cur
    if cur:
        cur.close()
    if conn:
        conn.close()

