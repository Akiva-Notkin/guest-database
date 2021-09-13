from bottle import route, run, template, post, request, static_file
from db_queries import insert_new_guest_into_db, insert_guest_to_stay_into_db, get_all_guests

@route('/hello')
def hello():
    return "Hello World!"

@route('/insert_new_guest')
def insert_new_guest_form():
    return static_file('insert_new_guest.html', root="./views")


@post('/insert_new_guest')
def insert_new_guest():
    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')
    also_known_as = request.forms.get('also_known_as')
    gender = request.forms.get('gender')
    date_of_birth = request.forms.get('date_of_birth')
    date_of_birth_year, date_of_birth_month, date_of_birth_day = date_of_birth.split("-")
    date_of_birth = f"{date_of_birth_month}/{date_of_birth_day}/{date_of_birth_year}"
    insert_new_guest_into_db(first_name=first_name, last_name=last_name, also_known_as=also_known_as, gender=gender,
                             date_of_birth=date_of_birth)


@route('/add_guest_to_stay')
def add_guest_to_stay_form():
    guests = get_all_guests()
    guests = [(f"{guest[2]} {guest[3]}", guest[0]) for guest in guests]
    return template('add_guest_to_stay', guests=guests)

@post('/add_guest_to_stay')
def add_guest_to_stay():
    guest_id = request.forms.get('guest_id')
    date_of_stay = request.forms.get('date_of_stay')
    notes = request.forms.get('notes')
    insert_guest_to_stay_into_db(guest_id=guest_id, date_of_stay=date_of_stay, notes=notes)

run(host='localhost', port=8080, debug=True)