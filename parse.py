##### Imports #####
import argparse
import getpass as gp

##### Custom modules #####
from stash_secret import stash_secret
from unstash_secret import unstash_secret
from peek_stash import peek_stash
from reveal_secret import reveal_secret
from authenticate import authenticate_user, ask_password

def parser():
    parser = argparse.ArgumentParser(description='SecretStash')

    ##### Password #####
    parser.add_argument('--password', '-p',default=gp.getpass(), help='Authenticate with password')
    
    subparsers = parser.add_subparsers(dest='command',help='Command to perform')

    ##### Stash #####
    stash_parser = subparsers.add_parser('stash', help='Add a secret to the SecretStash database')
    stash_parser.add_argument('website', help='Website secret is used for')
    stash_parser.add_argument('account', help='Account secret is used for')
    stash_parser.add_argument('secret', help='Secret itself, leave empty for an auto-created password', nargs='?', default='')

    ##### Unstash #####
    unstash_parser = subparsers.add_parser('unstash', help='Remove a secret from the SecretStash database')
    unstash_parser.add_argument('id', help='Id of the secret that should be removed')
    unstash_parser.add_argument('-f', '--force', action='store_true', help='Force delete secret')

    ##### Peek #####
    peek_parser = subparsers.add_parser('peek', help='Show all secrets stored, censored')

    ##### Reveal #####
    reveal_parser = subparsers.add_parser('reveal', help='Show secret of chosen id, uncensored')
    reveal_parser.add_argument('id', help='Id of secret that should be shown')

    args = parser.parse_args()

    ##### Authenticate the user before calling the functions #####
    if authenticate_user(args.password):

        if args.command == 'stash':
            stash_secret(website=args.website, account=args.account, secret=args.secret, password=args.password)
        elif args.command == 'unstash':
            unstash_secret(id=args.id, force_delete=args.force, password=args.password)
        elif args.command == 'reveal':
            reveal_secret(id=args.id, password=args.password)
        elif args.command == 'peek':
            peek_stash(password=args.password)
        else:
            print("Invalid command. Use one -h to see the commands")
