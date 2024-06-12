import sqlite3 
import json



conn = sqlite3.connect("contacts.db")
cur = conn.cursor()


example = {
    "contacts" : [
        {
            "name": "myname",
            "mobile": "123-332-444",
            "home": "4313213123"

        }
    ]
}


# cur.execute("""CREATE TABLE contacts ("id" INTEGER NOT NULL, 
#  "name" TEXT NOT NULL,
#   "mobile" TEXT,
#   "home" TEXT ,                                       
# PRIMARY KEY ("id" AUTOINCREMENT))""")


def create(data):
    for contact in data["contacts"]:        
        try:
          cur.execute(f"INSERT INTO contacts (name, mobile, home) VALUES (?, ?, ?)", (contact["name"], contact["mobile"], contact["home"]))

        except sqlite3.OperationnalError as err:
            print(err)
            return 
        conn.commit()
        print("New Record added!")
        return 
    

def read(name=None):
    if not name:
        name = ""


    cur.execute(f'SELECT * FROM contacts WHERE "name" LIKE "%{name}%"') 
    rows = cur.fetchall()
    records = {"results": []}


    for row in rows:
        record = {"name": row[1], "mobile": [2], "home": row[3]}
        records["results"].append(record)


    pretty_records = json.dumps(records, indent=2)

    print(pretty_records)
    return

def  _update_number(row):
    mobile = input("Enter a n mobile number (skip to leave)")
    home = input("Enter a new nubmer (skip to leave)")


    mobile = mobile if mobile != "" else row[2]
    home = home if home != "" else row[3    ] 

    cur.execute(f'UPDATE contacts SET mpbile ="{mobile}", home="{home}" '
                f'WHERE name="row[1]"')
    
    conn.commit()
    return

def update(name):
    cur.execute(f'SELECT * FROM contacts WHERE "name" LIKE "%{name}%"')
    rows = cur.fetchall()

    if len(rows) == 1:
        row = rows[0]
        _update_number(row)
    else:
        print("Mulrreweqeq result")

        for row in rows:
            print(row)


        _id = input("Enter number here:")
        cur.execute(f'SELECT * FROM contacts WHERE id={_id}')
        row = cur.fetchall()[0]
        _update_number(row)

        print("Number update succefully")
        return



def _delete_number(row):

    cur.execute(f'DELETE FROM contacts WHERE id={row[0]}')
    conn.commit()
    return






def delete(name):
    cur.execute(f'SELECT * FROM contacts WHERE "name" LIKE "%{name}%"')
    rows = cur.fetchall()

    if len(rows) == 1:
        row = rows[0]
        _delete_number(row)
    else:
        print("Mulrreweqeq result")

        for row in rows:
            print(row)


        _id = input("Enter number here:")
        cur.execute(f'SELECT * FROM contacts WHERE id={_id}')
        row = cur.fetchall()[0]
        _delete_number(row)

        print("Number deleted succefully")
        return






def main():
    while True:
        options = input("Create (c) Read(R) Update (U) Delete (D) Quit (q)")

        if options.lower() == 'c':
           new_record = {
               "contacts": [ 
                {
                    "name": input("Enter a name: "),
                    "mobile": input("Enter a mobile number"),
                    "home": input("Enter a home number")
                }

               ]

           }
           create(new_record)
        elif options.lower() == 'c':
              name = input("Enter a name")
              read(name)
        elif options.lower() == 'u':
               name = input("Enter a name")
               update(name)
        elif options.lower() == 'd':
               name = input("Enter a name")
               delete(name)
        elif options.lower() == 'q':
              print("Bye Bye")
              quit()
        else:
          print(f"No option {options} available")
        
    


if name == "main":
    main()