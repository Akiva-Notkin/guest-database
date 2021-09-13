import sqlite3
from sqlite3 import Error

database = r"C:\Users\akiva\WebstormProjects\guest-database\sqlite.db"


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def insert_new_guest_into_db(first_name, last_name, also_known_as, gender, date_of_birth, conn=None):
    """
    Insert new rows in the guests table
    :param date_of_birth:
    :param gender:
    :param also_known_as:
    :param last_name:
    :param first_name:
    :param conn: the Connection object
    :return:
    """
    if conn is None:
        conn = create_connection(database)
    cur = conn.cursor()
    birthday_month, birthday_day, birthday_year = date_of_birth.split("/")
    local_id = first_name[0] + last_name[0] + birthday_month + birthday_day
    insert_string = f"INSERT INTO guests (local_id, first_name, last_name, also_known_as, gender, date_of_birth) " \
                    f"VALUES('{local_id}', '{first_name}', '{last_name}', '{also_known_as}', '{gender}', " \
                    f"'{date_of_birth}') "

    cur.execute(insert_string)
    conn.commit()


def insert_guest_to_stay_into_db(guest_id, date_of_stay, notes, conn=None):
    """
    Inserts a new guest who is staying into the stays table
    :param guest_id:
    :param date_of_stay:
    :param notes:
    :param conn:
    :return:
    """
    if conn is None:
        conn = create_connection(database)
    cur = conn.cursor()

    insert_string = f"INSERT INTO stays (guest_id_stays, date_of_stay, notes)" \
                    f"VALUES({guest_id}, '{date_of_stay}', '{notes}')"

    cur.execute(insert_string)
    conn.commit()


def get_all_guests(conn=None):
    if conn is None:
        conn = create_connection(database)
    cur = conn.cursor()

    select_string = f"SELECT * FROM guests"

    cur.execute(select_string)

    rows = cur.fetchall()
    return rows
