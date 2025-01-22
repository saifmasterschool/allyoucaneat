import requests


def create_team(api_url, team_name):

    payload = {'teamName' : team_name}

    response = requests.post(api_url , json = payload)

    if response.status_code == 200:
        print(f'Team: {team_name} created successfully!')
        return response.json()
    else:
        print('Team name creation failed')
        print('Response:', response.text)


def register_number(api_url, ph_num):
    payload = {
  "phoneNumber": int(ph_num[1:]),
  "teamName": "WolvesofWallStreet"
}

    response = requests.post(api_url , json = payload)

    if response.status_code == 200:
        print(f'Phone number {ph_num} was registered successfully')
        send_sms(api_url, ph_num, 'Welcome to Wolves of Wall Street APP!')
        #return response.json()
    else:
        print('Phone number registration failed failed')
        print('Response:', response.text)

def unregister_number(api_url, ph_num):
    payload = {
  "phoneNumber": ph_num,
  "teamName": "WolvesofWallStreet"
}

    response = requests.post(api_url , json = payload)

    if response.status_code == 200:
        print(f'Phone number {ph_num} was unregistered successfully')
        send_sms(api_url, ph_num,f'Phone number {ph_num} was unregistered successfully')
        #return response.json()
    else:
        print('Phone number registration failed failed')
        print('Response:', response.text)


def send_sms(api_url, ph_num, message):
    payload = {
  "phoneNumber": int(ph_num[1:]),
  "message": message
    }

    response = requests.post(api_url, json = payload)

    if response.status_code == 200:
        print(f'Your message sent successfully')
        #return response.json()
    else:
        print('Message not delivered')
        print('Response:', response.text)


def retrieve_sms(API_URL_retrieve_sms):
    response = requests.get(API_URL_retrieve_sms)

    if response.status_code == 200:
        messages = response.json()
        return messages

    else:
        print(f'Error: {response.status_code}')


def check_sms():
    message = retrieve_sms(API_URL_retrieve_sms)

    if 'WolvesofWallStreet' in message:
        return "REGISTER"
    else:
        return "STOCK"


if __name__ == "__main__":

    API_URL_create_team = 'http://hackathons.masterschool.com:3030/team/addNewTeam'
    API_URL_register_num = 'http://hackathons.masterschool.com:3030/team/registerNumber'
    API_URL_send_sms = 'http://hackathons.masterschool.com:3030/sms/send'
    API_URL_retrieve_sms = 'http://hackathons.masterschool.com:3030/team/getMessages/WolvesofWallStreet'
    TeamName = 'WolvesofWallStreet'

    #create_team(API_URL_create_team, TeamName)

    ph_num = input('Please enter your German number without space and + sign')



    register_number(API_URL_register_num, ph_num)

    send_sms(API_URL_send_sms, ph_num)

    messages = retrieve_sms(API_URL_retrieve_sms)
    print(messages)