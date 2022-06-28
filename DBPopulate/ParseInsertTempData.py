from datetime import datetime
import csv
import psycopg2
import os
from psycopg2 import Error


def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

def get_binary_array(path):
    with open(path, "rb") as image:
        f = image.read()
        b = bytes(f).hex()
        return b

def insertUsers (connection):
    try:
        cursor = connection.cursor()
    except:
        print("couldn't set cursor to connection")
    cursor.execute("INSERT INTO Users(user_id, username, email, password_hash)" +
    " VALUES(%s,%s,%s,%s)", ("USR-001", "benk", "benk01@hotmail.com", "123"))
    connection.commit()

def insertLocations(connection):
    try:
        cursor = connection.cursor()
    except:
        print("couldn't set cursor to connection")
    image_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../Resources', 'southside.jpg'))
    opening_hours = '{07:30, 07:30, 07:30, 07:30, 07:30, 08:30, 08:30}'
    closing_hours = '{17:00, 17:00, 17:00, 17:00, 17:00, 17:00, 17:00}'
    cursor.execute("INSERT INTO Locations(location_id, location_name, address, location_pic, opening_hours, closing_hours)" +
    " VALUES(%s,%s,%s,%s,%s,%s)", ("LOC-001", "Southside Cafe", "1395 NE Stadium Way, Pullman, WA 99163", str(get_binary_array(image_path)), opening_hours, closing_hours))

    opening_hours = '{10:30, 10:30, 10:30, 10:30, 10:30, 10:30, 10:30}'
    closing_hours = '{17:00, 17:00, 17:00, 17:00, 17:00, 17:00, 17:00}'
    image_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../Resources', 'northside.jpg'))
    cursor.execute("INSERT INTO Locations(location_id, location_name, address, location_pic, opening_hours, closing_hours)" +
    " VALUES(%s,%s,%s,%s,%s,%s)", ("LOC-002", "Northside Cafe", "1580 NE Cougar Way, Pullman, WA 99164", str(get_binary_array(image_path)), opening_hours, closing_hours))

    image_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../Resources', 'hillside.jpg'))
    cursor.execute("INSERT INTO Locations(location_id, location_name, address, location_pic, opening_hours, closing_hours)" +
    " VALUES(%s,%s,%s,%s,%s,%s)", ("LOC-003", "Hillside Cafe", "650 NE Campus St, Pullman, WA 99163", str(get_binary_array(image_path)), opening_hours, closing_hours))
    connection.commit()

def parseFoodData(connection):
    try:
        cursor = connection.cursor()
    except:
        print("couldn't set cursor to connection")

    with open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), './food.csv')),'r') as f: 
        csvreader = csv.reader(f)
        next(csvreader)
        count_line = 0
        #read each JSON abject and extract data
        for line in csvreader:
            food_id = "FOOD-" + line[0]
            food_name = line[1]
            food_desc = line[3]
            image_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../Resources', 'Red_Apple.jpg'))    # line[14] is image path
            food_pic = str(get_binary_array(image_path))
            location_id = "LOC-" + line[2]
            avail_days = [bool(int(line[4])), bool(int(line[5])), bool(int(line[6])), bool(int(line[7])), bool(int(line[8])), bool(int(line[9])), bool(int(line[10]))]
            avail_times = [bool(int(line[11])), bool(int(line[12])), bool(int(line[13]))]

            
            cursor.execute("INSERT INTO FoodItems(food_id, food_name, food_pic, food_description)" +
            " VALUES(%s,%s,%s,%s)" + " ON CONFLICT (food_id) DO NOTHING", (food_id, food_name, food_pic, food_desc))

            connection.commit()

            cursor.execute("INSERT INTO FoodAvailability(avail_days, avail_times, food_id, location_id)" +
            " VALUES(%s,%s,%s,%s)", (avail_days, avail_times, food_id, location_id))

            connection.commit()
            count_line += 1
    print("FoodItems parsed: " + str(count_line))    
    f.close()
    


            



            


if __name__ == "__main__":
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="cougbites")
    except:
        print("couldn't connect")
    # read the JSON file
    # We assume that the Yelp data files are available in the current directory. If not, you should specify the path when you "open" the function. 
    #insertUsers(connection)
    #insertLocations(connection)
    parseFoodData(connection)

