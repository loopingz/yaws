import ConfigParser
import os
import argparse
import boto3
import sys

def main():
    parser = argparse.ArgumentParser(description='Loopingz AWS utilities')
    parser.add_argument('--profile', default='default', help='AWS Profile to use')
    parser.add_argument('command', choices=['export','rotate-keys'],help='Command to execute export|rotate-keys')
    args = parser.parse_args()
    profile = args.profile

    config = ConfigParser.ConfigParser()
    region = 'us-east-1'
    try:
        config.read(os.path.expanduser('~/.aws/config'))
        region = config.get('profile ' + profile, 'region', 'us-east-1')
    except:
        pass
    config.read(os.path.expanduser('~/.aws/credentials'))
    access_key = config.get(profile, 'aws_access_key_id')
    secret_key = config.get(profile, 'aws_secret_access_key')


    if args.command == 'export':
        print 'export AWS_ACCESS_KEY_ID='+access_key
        print 'export AWS_SECRET_ACCESS_KEY='+secret_key
        print 'export AWS_DEFAULT_REGION='+region
    elif args.command == 'rotate-keys':
        iam = boto3.client('iam', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
        keys = iam.list_access_keys()
        current_key = None
        other_key = None
        for _key in keys['AccessKeyMetadata']:
            if _key['AccessKeyId'] == access_key:
                current_key = _key
            else:
                other_key = _key
        if len(keys['AccessKeyMetadata']) > 1:
            print('Cannot rotate key %s as another key exists %s\n' % (access_key, other_key['AccessKeyId']))
            sys.exit(1)
        if not access_key:
            print('Cannot find key %s\n' % (access_key,))
            sys.exit(1)
        new_key = iam.create_access_key(UserName=current_key['UserName'])['AccessKey']
        config.set(profile, 'aws_access_key_id', new_key['AccessKeyId'])
        config.set(profile, 'aws_secret_access_key', new_key['SecretAccessKey'])
        config.write(open(os.path.expanduser('~/.aws/credentials'), 'w'))
        iam.delete_access_key(UserName=current_key['UserName'], AccessKeyId=access_key)
        print ('New key is %s\n' % (new_key['AccessKeyId'],))

if __name__ == '__main__':
    main()