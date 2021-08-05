import winsound, time
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import threading

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

# Tick Symbol
def tick():
    symbol = '\u2713'
    return symbol

def default_search():
    keywords = ['Internet Archive', 'archive.org', 'Borrow']
    inbox = 0
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('gbeep.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])
    # userInfo = service.users().getProfile(userId='me').execute()
    time.sleep(2)
    print(f"Logging Gmail {tick()}")
    time.sleep(2)
    print(f"Searching Mails {tick()}")
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        message = msg['snippet']
        for key in keywords:
            if key.lower() in message.lower():
                inbox += 1
                time.sleep(1)
                print(f"\nSearching for Keyword : {key}")
                print("One message found which matches the keyword")
                print(f'{message}\n')
                winsound.Beep(440, 500)
                winsound.Beep(370, 500)
                winsound.Beep(392, 500)
                if inbox > 5:
                    print(f"\nKeyword : {key}")
                    print("One new Mail Found")
                    print(f'{message}\n')
                    winsound.Beep(440, 500)
                    winsound.Beep(370, 500)
                    winsound.Beep(392, 500)
                else:
                    print("No new mails")
    if not messages:
        print("No messages found.")
    else:
        print("Message snippets:")
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            print(msg['snippet'])
    # User Profile
    # userInfo = service.users().getProfile(userId='me').execute()


def custom_search():
    c_keywords = []
    print("welcome to SherKey, what mails do you want me to search in your inbox ?")
    print("Press 'x' for execution")
    def key_log():
        key_word = input("Keys : ")
        if key_word == 'h':
            menu()
        elif key_word == 'x':
            def screen():
                time.sleep(2)
                print(f"Logging Gmail {tick()}")
                time.sleep(2)
                print(f"Searching Mails {tick()}")
            def pass_cmd():
                pass
            sc = threading.Thread(target=screen)
            cm = threading.Thread(target=pass_cmd)
            sc.start()
            time.sleep(3)
            cm.start()
        else:
            c_keywords.append(key_word)
            key_log()
        return c_keywords
    key_log()
    inbox = 0
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('gbeep.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])
    userInfo = service.users().getProfile(userId='me').execute()
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        message = msg['snippet']
        for key in c_keywords:
            if key.lower() in message.lower():
                inbox += 1
                print(f"\nKeyword : {key}")
                print("One message found which matches the keyword")
                print(f'{message}\n')
                winsound.Beep(440, 500)
                winsound.Beep(370, 500)
                winsound.Beep(392, 500)
                if inbox > 1:
                    print(f"\nKeyword : {key}")
                    print("One new Mail Found")
                    print(f'{message}\n')
                    winsound.Beep(440, 500)
                    winsound.Beep(370, 500)
                    winsound.Beep(392, 500)
                else:
                    print("No new mails")
    if not messages:
        print("No messages found.")
    else:
        print("Message snippets:")
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            print(msg['snippet'])


def sher_banner():
    print("""
                                                                                 
                                   ,_       
                                 ,'  `\,_   
                                 |_, -' _)    
                                 /##c  '\  (                   [ SherKey ] 
                                ' |'   -{.  )                  [ Developer : Mastermindx33 ]
                                  /\ __ -' \[]                 [ Version : 1.0 ]
                                 /`-_ `\     
                                 '      \  
                               _____    __                    __ __                      
                              / ___/   / /_   ___    _____   / //_/  ___    __  __       
                              \__ \   / __ \ / _ \  / ___/  / ,<    / _ \  / / / /       
                             ___/ /  / / / //  __/ / /     / /| |  /  __/ / /_/ /        
                            /____/  /_/ /_/ \___/ /_/     /_/ |_|  \___/  \__, /         
                                                                         /____/                                   
""")


def keyword_banner():
    print("""
                                        ,N.
                                      _/__ \        If you eliminate all other possibilities
                                       -/o\_\       the one that remains, however unlikely,
                                     __\_-./        is the right answer.
                                    / / V \`U-.
                        ())        /, > o <    \    Elementary my dear Watson.
                        <\.,.-._.-" [-\ o /__..-'  
                        |/_  ) ) _.-"| \o/  |  \ o!0
                           `'-'-" 
    """)


def menu():
    sher_banner()
    print("""
            1. Search
            2. Key Search
            """)
    opt = int(input(">> "))
    if opt == 1:
        default_search()
    elif opt == 2:
        keyword_banner()
        custom_search()
    elif opt == 'h':
        menu()


if __name__ == '__main__':
    menu()
