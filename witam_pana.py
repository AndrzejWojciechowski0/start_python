import argparse


parser = argparse.ArgumentParser(description='Powiedz: Witam serdecznie pana --name')
parser.add_argument('--name', type=str, help='Twoje imie prosze Pana!')


args = parser.parse_args()

print('Witam serdecznie pana ' + args.name)