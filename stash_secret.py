from sql import execute_query

def stash_secret(website, email, secret):
    ##### Print back #####
    censored_secret = ''

    ##### Sensor secret #####
    for i in secret:
        censored_secret += '*'

    print(f'Creating secret: {website}, {email}, {censored_secret}')

