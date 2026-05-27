import yaml

with open("company.yml", "r") as file:
    data = yaml.safe_load(file)

print(data)