import argparse


parser = argparse.ArgumentParser(description='Powiedz: Witam serdecznie pana --name')
parser.add_argument('--name', type=str, help='Pańskie imię proszę Pana!')

args = parser.parse_args()

with open("my_name.txt", "w") as my_file:
  my_file.write(args.name)
