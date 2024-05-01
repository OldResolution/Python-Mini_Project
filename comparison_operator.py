
from system_info import *
import psycopg2
Dbname ='PyProject'
Username='postgres'
Password='Tejas'
Hostname='localhost'
Port= '5432'

conn=None
cur=None
def Compare_info(gamename):
    # Assuming you have a function to retrieve user hardware information from the database
    user_os, user_processor, user_ram, user_rom, user_gpu = Get_User_Info()

    # Assuming you have a database query function to retrieve hardware information of users who play the game
    user_hardware_info = game_info(gamename)
    #print (user_hardware_info['RAM'])
    #print (user_ram)

    # Compare user's hardware information with system information
    if user_hardware_info:
        matched_criteria = []
        #if user_os == user_hardware_info['OS']:
           # matched_criteria.append('OS')
        if user_processor >= user_hardware_info['Processor']:
            matched_criteria.append('Processor')
        else:
            return "Processor in incompatible." 
        if user_ram <= user_hardware_info['RAM']:
            matched_criteria.append('RAM')
           # return "RAM in compatible."
        else:
            return "RAM in incompatible."
        #if user_rom >= user_hardware_info['ROM']: 
           # matched_criteria.append('ROM')
        if user_gpu == user_hardware_info['GPU']:
            matched_criteria.append('GPU')    
        else:
            return "GPU is incompatible."

        if len(matched_criteria) == 0:
            return "No user matches the hardware criteria for this game."
        else:
            return f"The following criteria matched for users playing {gamename}: {', '.join(matched_criteria)}"
    else:
        return "No user hardware information found for this game."

def connect_to_database():
    try:
        # Connect to the database
        conn = psycopg2.connect(
            dbname=Dbname,
            user=Username,
            password=Password,
            host=Hostname,
            port=Port
        )
        return conn

    except psycopg2.Error as e:
        return None, f"Error connecting to the database: {e}"

#def Processor_Rating(user_processor):

#def GPU_Rating(user_processor):
# Function to retrieve user's hardware information from the database
def game_info(gamename):
    # Assuming you have a database connection and cursor established
    try:
        conn = connect_to_database()
        cur = conn.cursor()

        # Assuming you have a table named 'user_hardware_info' with columns 'game_name', 'OS', 'Processor', 'RAM', 'ROM', 'GPU'
        cur.execute("SELECT * FROM game_requirements WHERE game_title = %s", (gamename,))
        user_hardware_info = cur.fetchone()

        if user_hardware_info:
            hardware_info = {
                'OS': user_hardware_info[2],
                'Processor': user_hardware_info[4],
                'RAM': user_hardware_info[6],
                #'ROM': user_hardware_info[4],
                'GPU': user_hardware_info[8]
            }
            return hardware_info
        else:
            return None

    except psycopg2.Error as e:
        print(f"Error retrieving user hardware information: {e}")
        return None

    finally:
        # Close cursor and connection
        if cur:
            cur.close()
        if conn:
            conn.close()

print (game_info("GTA 5"))