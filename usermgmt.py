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


def register_numbers(api_url, ph_num):
    payload = {
  "phoneNumber": ph_num,
  "teamName": "allyoucaneat"
}

    response = requests.post(api_url , json = payload)

    if response.status_code == 200:
        print(f'Phone number {ph_num} was registered successfully')
        #return response.json()
    else:
        print('Phone number registration failed failed')
        print('Response:', response.text)

def send_sms(api_url):
    payload = {
  "phoneNumber": <ph number>,
  "message": 'Welcome to Allyoucaneat APP!'
    }

    response = requests.post(api_url, json = payload)

    if response.status_code == 200:
        print(f'Your message sent successfully')
        #return response.json()
    else:
        print('Message not delivered')
        print('Response:', response.text)


def retrieve_sms(api_url):

    response = requests.get(API_URL_retrieve_sms)

    if response.status_code == 200:
        messages = response.json()
        return messages

    else:
        print(f'Error: {response.status_code}')


if __name__ == "__main__":
    API_URL_create_team = 'http://hackathons.masterschool.com:3030/team/addNewTeam'
    API_URL_register_num = 'http://hackathons.masterschool.com:3030/team/registerNumber'
    API_URL_send_sms = 'http://hackathons.masterschool.com:3030/sms/send'
    API_URL_retrieve_sms = 'http://hackathons.masterschool.com:3030/team/getMessages/allyoucaneat'
    TeamName = 'allyoucaneat'

    #create_team(API_URL_create_team,TeamName)

    phone_num = input('Please enter your German number without space and + sign')

    register_numbers(API_URL_register_num, phone_num)

    send_sms(API_URL_send_sms)

    messages = retrieve_sms(API_URL_retrieve_sms)
    for user_id, message_list in messages.items():
        print(f"\nMessages for User ID {user_id}:")
        for msg in message_list:
            text = msg.get("text", "No text")
            received_at = msg.get("receivedAt", "Unknown time")
            print(f"  - {text} (Received at: {received_at})")
