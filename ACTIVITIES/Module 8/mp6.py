import sys
import pymysql
import ast



def addItemToDB(i_id, name, desc, price):
    q = "INSERT INTO items (`id`, `name`, `description`, `price`) VALUES ('{}', '{}', '{}', '{}') ".format(i_id, name, desc, price)
    try:
        print("execute")
        cur.execute(q)
        print("commit")
        db.commit()
        print('added to db')
    except Exception as e:
        db.rollback()
        print(e)
        print('adding to db failed')

def whatToEdit(i_id,trow):
    row = list(trow)
    s=''
    inp = 'something'
    while inp != '0':
        print(f'ID{s:<9}Name{s:<9}Description{s:<9}Price')
        print(f"{row[0]:<11}{row[1]:<13}{row[2]:<20}{row[3]}")
        print('[1]id')
        print('[2]name')
        print('[3]description')
        print('[4]price')
        print('[0]done/back')
        inp = input('your choice: ')

        if inp == '1':
            row[0] = input('enter new id:')

        elif inp == '2':
            row[1] = input('enter new name:')

        elif inp == '3':
            row[2] = input('enter new description:')
        
        elif inp == '4':
            row[3] = input('enter new price:')
        
        else:
            pass
    q = "UPDATE items SET id=%s,name=%s,description = %s,price = %s WHERE id = %s"
    try:
        print("execute")
        values = (row[0], row[1],row[2],row[3],i_id)
        cur.execute(q, values)
        print("commit")
        db.commit()
        print('edited db')
    except Exception as e:
        db.rollback()
        print(f'error: {e}')

def editItem(i_id):
    data = fetchData()
    try:
        for row in data:
            if row[0] == i_id:
                choice = input(f'are you sure? to edit {row[1]} [y/n]: ')
                if choice == 'y' or 'Y':
                    whatToEdit(i_id,row)
                else:
                    pass
    except Exception as e:
        print(f'no item with id number {i_id}{e}')

def deleteItem(i_id):
    data = fetchData()
    try:
        for row in data:
            if row[0] == i_id:
                choice = input(f'are you sure to delete {row[1]}?  [y/n]: ')
                if choice == 'y' or 'Y':
                    q = "DELETE FROM items WHERE id = %s"
                    print('execute')
                    cur.execute(q, i_id)
                    print("commit")
                    db.commit()
                    print('item deleted')
                else:
                    pass
    except Exception as e:
        print(f'no item with id number {i_id}')


def fetchData():
    q = "select * from items"
    cur.execute(q)
    data = cur.fetchall()
    return data
    
def displayItems():
    s = ''
    print(f'ID{s:<9}Name{s:<9}Description{s:<9}Price')
    data=fetchData()
    for row in data:
        print(f"{row[0]:<11}{row[1]:<13}{row[2]:<20}{row[3]}")

def openMain ():
    inp = 'something'
    while inp != '0':
        print('[1]add')
        print('[2]edit')
        print('[3]delete')
        print('[4]display items')
        print('[0]exit')
        inp = input('your choice: ')

        if inp == '1':
            print ('add item')
            i_id = input('id: ')
            name = input('Name: ')
            desc = input('Description: ')
            price = input('Price: ')
            addItemToDB(i_id, name, desc, price)
        elif inp == '2':
            print ('edit item')
            displayItems()
            id = input('enter id to edit: ')
            editItem(id)
        elif inp == '3':
            print ('delete')
            displayItems()
            id = input('enter id to delete: ')
            deleteItem(id)
        elif inp == '4':
            print('Item List')
            displayItems()
        else:
            pass
        

if __name__ == '__main__':
    try:
        print("Connecting to DB")
        db = pymysql.connect("localhost", "root", "", "mp6")
        cur = db.cursor()
        print("Succesfully connected to DB")
        print("Starting program...")
        openMain()
        cur.close()
        db.close()
        print("Exiting program")
    except pymysql.DatabaseError:
        print('sorry cannot connect to the database')
        sys.exit()
    except:
        print ('Exiting program')