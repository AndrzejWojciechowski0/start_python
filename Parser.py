import argparse


parser = argparse.ArgumentParser(description='Powiedz: Witam serdecznie pana --name')
parser.add_argument('--name', type=str, help='Pańskie imię proszę Pana!')
parser.add_argument("--secondname", type=str, help='Pańskie nazwisko Panie! --secondname')


args = parser.parse_args()

print("Witam serdzecznie Pana o imieniu " + args.name)
print("Witam serdzecznie Pana o nazwisku" + args.secondname)
print("Witam serdzecznie Pana " + args.name + args.secondname)
