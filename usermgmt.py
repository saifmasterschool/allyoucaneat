import sys
import requests


def create_team(team_name):
    """ Creates a team name"""
    api_url_create_team = 'http://hackathons.masterschool.com:3030/team/addNewTeam'
    payload = {'teamName': team_name}
    response = requests.post(api_url_create_team, json=payload)

    if response.status_code == 200:
        print(f'Team: {team_name} created successfully!')
        return response.json()
    else:
        print('Team name creation failed')
        print('Response:', response.text)


def register_number(ph_num):
    """ registers a number"""
    api_url_register_num = 'http://hackathons.masterschool.com:3030/team/registerNumber'
    payload = {"phoneNumber": ph_num,
               "teamName": "wows"}

    response = requests.post(api_url_register_num, json=payload)

    if response.status_code == 200:
        print(f'Phone number {ph_num} was registered successfully')
        send_sms(ph_num, 'Welcome to Wolves of Wall Street APP!\n Answer to this number to get options')
    else:
        print('Phone number registration failed')
        print('Response:', response.text)


def unregister_number(ph_num):
    "unsubscribes a number"
    api_url_unregister_num = 'http://hackathons.masterschool.com:3030/team/unregisterNumber'
    payload = {"phoneNumber": ph_num,
               "teamName": "wows"}

    response = requests.post(api_url_unregister_num, json=payload)

    if response.status_code == 200:
        print(f'Phone number {ph_num} was unregistered successfully')
        send_sms(ph_num, f'Phone number {ph_num} was unregistered successfully')
    else:
        print('Phone number unregistration failed')
        print('Response:', response.text)


def send_sms(ph_num, message):
    """sends sms"""
    api_url_send_sms = 'http://hackathons.masterschool.com:3030/sms/send'
    payload = {
        "phoneNumber": int(ph_num),
        "message": message,

    }

    response = requests.post(api_url_send_sms, json=payload)

    if response.status_code == 200:
        print(f'Your message "{message}" sent successfully')
    else:

        print('Message not delivered')
        print('Response:', response.text)


def retrieve_sms():
    "retrieves messages"
    api_url_retrieve_sms = 'http://hackathons.masterschool.com:3030/team/getMessages/wows'
    response = requests.get(api_url_retrieve_sms)

    if response.status_code == 200:
        messages = response.json()
        return messages
    else:
        print(f'Error: {response.status_code}')
        print('Response:', response.text)


def print_menu():
    """ prints menu"""
    print("\n0. Exit"
          "\n1. Register User"
          "\n2. Unregister User"
          "\n3. Send Message"
          "\n4. List Registered Users\n")


def menu_logic(user_input):
    """ menu logic"""
    if user_input == '0':
        sys.exit()
    if user_input == '1':
        ph_num = input('Please enter your German number without space and + sign: ')
        register_number(ph_num)
    if user_input == '2':
        ph_num = input('Please enter your Phone number without space and + sign: ')
        unregister_number(ph_num)
    if user_input == '3':
        ph_num = input('Please enter your Phone number without space and + sign: ')
        message = input('Please enter your message: ')
        send_sms(ph_num, message)
    if user_input == '4':
        messages = retrieve_sms()
        if messages:
            for key, value in messages.items():
                print(f'{key}{value}\n')


if __name__ == "__main__":
    while True:
        print_menu()
        user_input = input("Please enter option: ")
        menu_logic(user_input)
