#!/usr/bin/python3
print("Content-type:text/html \n\n")

import mysql.connector
from mysql.connector import Error
import base64

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="IMDB"
    )

    sql_select_Query = "SELECT * FROM mytable"

    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
   
    data_uri = base64.b64encode(open('download.jpeg', 'rb').read()).decode('utf-8')
    img_tag = '<center> <img src="data:image/jpeg;base64,{0}" class="img"> </center>'.format(data_uri)
    print(img_tag)

    print("<body id='box1'> <link rel='stylesheet' href='project.css'></body>")
    print("<br>")
    print("<center> <h1> Movies of 2019 </h1> </center>")

    
# print("\nPrinting each movie record")
    for row in records:
        print("<center><table border=3>")
        print("<td>")
        print("<br> MovieName : ", row[0],)
        print("</td>")
        print("<td>")
        print("<br> Date : ", row[1])
        print("</td>")
        print("<td>")
        print("<br> Votes  : ", row[2])
        print("</td>")
        print("<td>")
        print("<br> Rating : ", row[3])
        print("</td>")
        print("<td>")
        print("<br> PG : ", row[4])
        print("</td>")
        print("<td>")
        print("<br> Runtime : ", row[5])
        print("</td>")
        print("<td>")
        print("<br> Genre : ", row[6],)
        print("</td>")
        print("<br> </table> </center> <br>" "\n")


except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        # print("MySQL connection is closed")