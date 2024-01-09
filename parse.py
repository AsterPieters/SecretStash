##### Imports #####
import argparse

##### Custom modules #####
from stash_secret import stash_secret
from unstash_secret import unstash_secret

def parser():
    parser = argparse.ArgumentParser(description='SecretStash')
    subparsers = parser.add_subparsers(dest='command',help='Command to perform')

    ##### Stash #####
    stash_parser = subparsers.add_parser('stash', help='Add a secret to the SecretStash database')
    stash_parser.add_argument('website', help='Website secret is used for')
    stash_parser.add_argument('account', help='Account secret is used for')
    stash_parser.add_argument('secret', help='Secret itself')

    ##### Unstash #####
    unstash_parser = subparsers.add_parser('unstash', help='Remove a secret from the SecretStash database')
    unstash_parser.add_argument('id', help='Username')

    args = parser.parse_args()

    if args.command == 'stash':
        stash_secret(website=args.website, account=args.account, secret=args.secret)
    elif args.command == 'unstash':
        unstash_secret(id=args.id)
    else:
        print("Invalid command. Use 'stash' or 'unstash' command.")