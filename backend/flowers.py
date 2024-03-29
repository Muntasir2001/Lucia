import datetime
import random
from backend.graphs import readdata
from backend.enums import comunication
from backend.enums import FLowers
from backend.Chemicas import Chemichals
from backend.Chemicas import comunicationChem
from backend.prices import comunicationprices
from backend.prices import Prices
from backend.senzori.water.water import intoduce

import csv
from datetime import date
import os

def flowes():
        var = FLowers
        watercost = 1.0
        var = comunication("Rose")
        plants = random.randint(0, 167)
        intoduce(plants,var.value[5])
        varchem = Chemichals
        varchem = comunicationChem(var.value[2])

        #print(varchem.value[0])
        #print(" Name:", var.value[0], '\n', "Price:", var.value[1], " euros", '\n', "Chemichal:", var.value[2], '\n', "Themperature:", var.value[3], "Celsiu", '\n', "Luminosity", var.value[4], "Watts", '\n', "Waterperplant",var.value[5], "liters")

        sold = random.randint(0, plants)
        week = random.randint(14, 16)
        cost = ((watercost * var.value[5] * (plants / 10)) + varchem.value[1] * (plants / 8)) * week
        Profit = var.value[1] * sold
        Damage = var.value[1] * (plants - sold)
        #print("Plants:", plants, '\n', "Sold:", sold, '\n', "Profit:", Profit - cost, "euros", '\n', "Damage:", Damage, "euros", '\n', "Weeks", week, '\n', "Cost:", cost, '\n')


        Current_Date = datetime.datetime.now()  # datetime.datetime.today().strftime('%d-%b-%Y')

        with open(('./Csv_files/Production_' + str(Current_Date) + '.csv'), 'w') as new_file:
            csv.writer = csv.writer(new_file, delimiter=' ')

            csv.writer.writerow(['Name:', var.value[0]])
            csv.writer.writerow(['Price:', var.value[1], 'euros'])
            csv.writer.writerow(['Chemichal:', var.value[2]])
            csv.writer.writerow(['Themperature:', var.value[3], 'Celsiu'])
            csv.writer.writerow(['Luminosity', var.value[4], 'Watts'])
            csv.writer.writerow(['Waterperplant', var.value[5], 'liters'])
            csv.writer.writerow(['Plants:', plants])
            csv.writer.writerow(['Sold:', sold])
            csv.writer.writerow(['Profit:', Profit - cost, 'euros'])
            csv.writer.writerow(['Damage:', Damage, 'euros'])
            csv.writer.writerow(['Weeks', week])
            csv.writer.writerow(['Cost:', cost, 'euros'])