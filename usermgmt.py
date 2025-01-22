import sys
import requests



def create_team(team_name):

    api_url_create_team = 'http://hackathons.masterschool.com:3030/team/addNewTeam'

    payload = {'teamName' : team_name}

    response = requests.post(api_url_create_team , json = payload)

    if response.status_code == 200:
        print(f'Team: {team_name} created successfully!')
        return response.json()
    else:
        print('Team name creation failed')
        print('Response:', response.text)


def register_number( ph_num):

    api_url_register_num = 'http://hackathons.masterschool.com:3030/team/registerNumber'

    payload = {
  "phoneNumber": ph_num,
  "teamName": "wows"
}

    response = requests.post(api_url_register_num , json = payload)

    if response.status_code == 200:
        print(f'Phone number {ph_num} was registered successfully')
        api_url_send_sms = 'http://hackathons.masterschool.com:3030/sms/send'
        send_sms(api_url_send_sms, ph_num, 'Welcome to Wolves of Wall Street APP!')
        #return response.json()
    else:
        print('Phone number registration failed failed')
        print('Response:', response.text)

def unregister_number(ph_num):
    api_url_unregister_num = 'http://hackathons.masterschool.com:3030/team/unregisterNumber'
    payload = {
  "phoneNumber": ph_num,
  "teamName": "wows"
}

    response = requests.post(api_url_unregister_num , json = payload)

    if response.status_code == 200:
        print(f'Phone number {ph_num} was unregistered successfully')
        send_sms(ph_num,f'Phone number {ph_num} was unregistered successfully')

    else:
        print('Phone number registration failed failed')
        print('Response:', response.text)


def send_sms(ph_num, message):

    api_url_send_sms = 'http://hackathons.masterschool.com:3030/sms/send'

    payload = {
  "phoneNumber": ph_num,
  "message": message,

}

    response = requests.post(api_url_send_sms, json = payload)

    if response.status_code == 200:
        print(f'Your message "{message}" sent successfully')
        #return response.json()
    else:
        print('Message not delivered')
        print('Response:', response.text)


def retrieve_sms():
    api_url_retrieve_sms = 'http://hackathons.masterschool.com:3030/team/getMessages/wows'
    response = requests.get(api_url_retrieve_sms)

    if response.status_code == 200:
        messages = response.json()
        return messages

    else:
        print(f'Error: {response.status_code}')


def print_menu():
    print("\n0. Exit"
          "\n1. Register User"
          "\n2. Unregister User"
          "\n3. send_message",
          "\n4. List_registered_users\n")
4
def menu_logic(user_input):
    if user_input == '0':
        sys.exit()
    if user_input == '1':
        ph_num = input('Please enter your German number without space and + sign')
        register_number(ph_num)
    if user_input == '2':
        ph_num = input('Please enter your Phone number without space and + sign')
        unregister_number(ph_num)
    if user_input == '3':
        ph_num = input('Please enter your Phone number without space and + sign')
        message = input('Please enter your message')
        send_sms(ph_num, message)
    if user_input == '4':
        messages = retrieve_sms()
        for key in messages.keys():
            print(key)

if __name__ == "__main__":
    while True:
        print_menu()
        user_input = input("Please enter option: ")
        menu_logic(user_input)


