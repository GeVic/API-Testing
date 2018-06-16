import psycopg2
from flask import Flask, render_template, request, redirect, Response
import random, json
import sys

# creating flask object
app = Flask(__name__)

# to ensure the responses aren't cached (stored)
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

def search(pincode):
    duplicate = 0
    # inserting into database
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=gevic@@1@@")
        cur = conn.cursor()
        sql = "SELECT * from mapping WHERE pincode LIKE (%s);"
        cur.execute(sql, (pincode,))
        duplicate = len(cur.fetchall())
        conn.commit()
    except psycopg2.DatabaseError as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    if not(duplicate):
        return True
    else:
        return False    
    


# route the default page
@app.route('/')
def index():
    # to render map
    return render_template("index.html")

# post location
@app.route('/location', methods=['POST'])
def location():
    pincode =  request.form.get("pincode")
    place =  request.form.get("place")
    city =  request.form.get("city")
    key = "IN"
    try:
        longitude =  float(request.form.get("longitude"))
        latitude =  float(request.form.get("latitude"))
    except ValueError:
        return render_template("error.html", message = "Invalid longitude or latitude")

    # check of the data already exists
    isExist = search(pincode)
    
    if isExist:
        # inserting into database
        conn = None
        try:
            # connect to the PostgreSQL server
            conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=gevic@@1@@")
            cur = conn.cursor()
            sql = "INSERT INTO mapping(key, pincode, place_name, admin_name1, latitude, longitude) \
                    VALUES(%s, %s, %s, %s, %s, %s);"
            cur.execute(sql, (key, pincode, place, city, latitude, longitude))
            conn.commit()
        except psycopg2.DatabaseError as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        # render template        
        return render_template("post_location.html", pincode=pincode, place=place, city=city, longitude=longitude, latitude=latitude)
    else:
        return render_template("database.html")


if __name__ == '__main__':
	# run!
	app.run(debug=True)

# creating tables
def create_tables():
  
  conn = None
  try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=gevic@@1@@")
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE mapping (
                key VARCHAR(2) NOT NULL,
                pincode VARCHAR(20) NOT NULL,
                place_name VARCHAR(120) NOT NULL,
                admin_name1 VARCHAR(100),
                latitude  DECIMAL(12, 8),
                longitude DECIMAL(12, 8),
                accuracy VARCHAR(2)
        )
        """)
        
        # csv files
        with open('IN.txt', 'r') as f:
          next(f)  # Skip the header row.
          cur.copy_from(f, 'mapping', sep=',')
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
  except psycopg2.DatabaseError as error:
        print(error)
  finally:
        if conn is not None:
            conn.close()

    
