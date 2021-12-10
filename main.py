# QAP 5 - ONE STOP INSURANCE
# Dominic Whelan
# Dec.07, 2021

import datetime
import time
from dateutil.relativedelta import relativedelta

# Constants

f = open("OSICDef.dat", "r")

POL_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
ADD_CAR_DIS = float(f.readline())
EXTRA_LIA_COST = float(f.readline())
GLASS_COV_COST = float(f.readline())
LOAN_CAR_COV_COST = float(f.readline())        # PER CAR
HST_RATE = float(f.readline())                 # MULTIPLY BY SUB TOTAL FOR TAXES
PROC_FEE_RATE = float(f.readline())            # ADD TO POLICY TOTAL ALL DIVIDED BY 12 FOR MONTHLY PAYMENT

f.close()

# Validation purposes
allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
pos_code_alpha_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
digit_set = set("1234567890")

# Start of main program loop
while True:

    # Inputs

    while True:
        cus_first_name = input("Enter Customer's First Name: ").title()
        if cus_first_name == "":
            print("Must Enter First Name")
        elif not set(cus_first_name).issubset(allowed_char):
            print("Invalid Entry, Please Use A-Z,- or '")
        else:
            break

    while True:
        cus_last_name = input("Enter Customer's Last Name: ").title()
        if cus_last_name == "":
            print("Must Enter Last Name")
        elif not set(cus_last_name).issubset(allowed_char):
            print("Invalid Entry, Please Use A-Z,- or '")
        else:
            break

    while True:
        street_add = input("Enter Street Address: ").title()
        if street_add == "":
            print("Please Enter a Street Address")
        else:
            break

    while True:
        city = input("Enter City: ").title()
        if city == "":
            print("Please Enter City")
        else:
            break

    while True:
        province = input("Enter Province Code (XX): ").upper()
        if len(province) != 2:
            print("Must use 2 character code")
        elif province != "AB" and province != "BC" and province != "MB" and province != "NB" and province != "NL" and province != "NT" and province != "NS" and province != "NU" and province != "ON" and province != "PE" and province != "QC" and province != "SK" and province != "YT":
            print("Please use Valid Code")
        else:
            break

    while True:
        pos_code = input("Enter Postal Code (A1B2C3): ").upper()
        if pos_code == "":
            print("Please Enter Postal Code")
        elif len(pos_code) != 6:
            print("Postal Code Must be 6 Characters")
        elif set(pos_code[0]).issubset(pos_code_alpha_set) is False or set(pos_code[1]).issubset(digit_set) is False or set(pos_code[2]).issubset(pos_code_alpha_set) is False or set(pos_code[3]).issubset(digit_set) is False or set(pos_code[4]).issubset(pos_code_alpha_set) is False or set(pos_code[5]).issubset(digit_set) is False:
            print("Must be in specified format")
        else:
            break

    while True:
        phone_num = input("Enter Home Phone Number (1234567890): ")
        if len(phone_num) != 10:
            print("Please Enter 10 Digit Phone Number")
        elif set(phone_num).issubset(digit_set) is False:
            print("Please Use Digits 0-9 Only")
        else:
            break

    while True:
        try:
            num_cars = int(input("Number of vehicles to be insured: "))
        except:
            print("Invalid Entry, Try Again")
        else:
            if num_cars <= 0:
                print("Error, Value must be an Integer > 0")
            else:
                break

    while True:
        extra_lia = input("Extra Liability (Y/N): ").upper()
        if extra_lia != "Y" and extra_lia != "N":
            print("Please Enter 'Y' or 'N': ")
        else:
            break

    while True:
        glass_coverage = input("Glass Coverage (Y/N): ").upper()
        if glass_coverage != "Y" and glass_coverage != "N":
            print("Please Enter 'Y' or 'N': ")
        else:
            break

    while True:
        loaner_car = input("Loaner Car (Y/N): ").upper()
        if loaner_car != "Y" and loaner_car != "N":
            print("Please Enter 'Y' or 'N': ")
        else:
            break

    while True:
        pay_option = input("Pay in Full or Monthly ( F or M ): ").upper()
        if pay_option != "F" and pay_option != "M":
            print("Please Enter 'F' or 'M' ")
        else:
            break

    # Calculations

    pol_date = datetime.datetime.now()
    first_pay_due = datetime.datetime.now()     # Pre-defined variable

    add_day = datetime.timedelta(days=1)
    add_month = relativedelta(months=1)

    if pol_date.day > 25:
        first_pay_due += add_month

    while True:
        if first_pay_due.day != 1:
            first_pay_due += add_day
        else:
            break

    # _dsp represents display purposes on output
    pol_date_dsp = datetime.datetime.strftime(pol_date, "%d-%b-%y")
    first_pay_due_dsp = datetime.datetime.strftime(first_pay_due, "%d-%b-%y")

    ins_prem = BASIC_PREM

    if num_cars > 1:
        ins_prem += (BASIC_PREM - (ADD_CAR_DIS * BASIC_PREM)) * (num_cars - 1)

    extra_cost = 0

    if extra_lia == "Y":
        extra_cost += EXTRA_LIA_COST

    if glass_coverage == "Y":
        extra_cost += GLASS_COV_COST

    if loaner_car == "Y":
        extra_cost += LOAN_CAR_COV_COST * num_cars

    ins_prem_dsp = "${:,.2f}".format(ins_prem)
    extra_cost_dsp = "${:,.2f}".format(extra_cost)
    total_ins_prem = ins_prem + extra_cost
    total_ins_prem_dsp = "${:,.2f}".format(total_ins_prem)
    hst = total_ins_prem * HST_RATE
    hst_dsp = "${:,.2f}".format(hst)
    total_cost = hst + total_ins_prem
    total_cost_dsp = "${:,.2f}".format(total_cost)

    mon_payment = (total_cost + PROC_FEE_RATE) / 12
    mon_payment_dsp = "${:,.2f}".format(mon_payment)

    pos_code_dsp = "{} {}".format(pos_code[:3].upper(), pos_code[3:].upper())

    # Output

    print()
    print("ONE STOP INSURANCE             {}".format(pol_date_dsp))
    print("CUSTOMER POLICY SUMMARY          {}-{}{}".format(POL_NUM, cus_first_name[0].upper(), cus_last_name[0].upper()))
    print("                              {} vehicles".format(num_cars))
    print("-" * 40)
    print("Client: {}. {}".format(cus_first_name[0], cus_last_name))
    print("        {}".format(street_add))
    print("        {}, {} {}".format(city, province, pos_code_dsp))
    print()
    print("Policy base cost:              {:>9}".format(ins_prem_dsp))
    print("Extra costs:                   {:>9}".format(extra_cost_dsp))
    print("Subtotal:                      {:>9}".format(total_ins_prem_dsp))
    print("HST:                           {:>9}".format(hst_dsp))
    print("                               ---------")
    print("Policy total/Full payment:     {:>9}".format(total_cost_dsp))
    print()
    print("For monthly payment customers: ")
    print("   Monthly Payment:            {:>9}".format(mon_payment_dsp))
    print("   First payment date:         {}".format(first_pay_due_dsp))
    print()
    print("----------------------------------------")
    print("    \"ONE STOP - Insuring the world!\"")
    print()

    # Save policy records for future reference
    f = open("Policies.dat", "a")

    f.write("{}, ".format(POL_NUM))  # 0
    f.write("{}, ".format(cus_first_name))  # 1
    f.write("{}, ".format(cus_last_name))  # 2
    f.write("{}, ".format(street_add))  # 3
    f.write("{}, ".format(city))  # 4
    f.write("{}, ".format(province))  # 5
    f.write("{}, ".format(pos_code))  # 6
    f.write("{}-{}-{}, ".format(phone_num[:3], phone_num[3:6], phone_num[6:]))  # 7
    f.write("{}, ".format(num_cars))  # 8
    f.write("{}, ".format(extra_lia))  # 9
    f.write("{}, ".format(glass_coverage))  # 10
    f.write("{}, ".format(loaner_car))  # 11
    f.write("{}, ".format(pay_option))  # 12
    f.write("{}\n".format(ins_prem))  # 13

    f.close()

    POL_NUM += 1

    # Write all values back to default file
    f = open("OSICDef.dat", "w")

    f.write("{}\n".format(POL_NUM))
    f.write("{}\n".format(BASIC_PREM))
    f.write("{}\n".format(ADD_CAR_DIS))
    f.write("{}\n".format(EXTRA_LIA_COST))
    f.write("{}\n".format(GLASS_COV_COST))
    f.write("{}\n".format(LOAN_CAR_COV_COST))
    f.write("{}\n".format(HST_RATE))
    f.write("{}\n".format(PROC_FEE_RATE))

    f.close()

    print("Policy Processed and Saved")
    time.sleep(2)
    print()

    another_entry = input("Enter Another Policy? ( Y or N ): ").upper()
    if another_entry == "N":
        break

# Reports

print()
print("     PLEASE SEE BELOW FOR REPORTS    ")
print()

# Report Title
print("ONE STOP INSURANCE COMPANY")
print("POLICY LISTING AS OF {}".format(pol_date_dsp))
print()

# Report Heading
print("POLICY   CUSTOMER           INSURANCE     EXTRA     TOTAL")
print("NUMBER   NAME                PREMIUM      COSTS    PREMIUM")
print("===========================================================")

# Report Contents

pol_ctr = 0         # Count of the number of policies
prem_acc = 0        # Sum of Insurance Premiums
prem_acc_dsp = ""
extra_acc = 0       # Sum of Extra Costs
extra_acc_dsp = ""
tot_acc = 0         # Sum of Total Premiums
tot_acc_dsp = ""

f = open("Policies.dat", "r")

for line in f:

    data_obj = line.split(",")
    pol_num_rep = data_obj[0].strip()
    cus_name_rep = "{} {}".format(data_obj[1].strip(), data_obj[2].strip())
    ins_prem_rep = float(data_obj[13].strip())
    ins_prem_rep_dsp = "${:,.2f}".format(ins_prem_rep)

    extra_cost_rep = 0
    if data_obj[9].strip() == "Y":
        extra_cost_rep += EXTRA_LIA_COST
    if data_obj[10].strip() == "Y":
        extra_cost_rep += GLASS_COV_COST
    if data_obj[11].strip() == "Y":
        extra_cost_rep += LOAN_CAR_COV_COST

    extra_cost_rep_dsp = "${:,.2f}".format(extra_cost_rep)

    tot_prem = ins_prem_rep + extra_cost_rep
    tot_prem_rep = "${:,.2f}".format(tot_prem)

    print("{}   {:<20} {:>9}  {:>9}  {:>9}".format(pol_num_rep, cus_name_rep, ins_prem_rep_dsp, extra_cost_rep_dsp, tot_prem_rep))

    pol_ctr += 1
    prem_acc += ins_prem_rep
    prem_acc_dsp = "${:,.2f}".format(prem_acc)
    extra_acc += extra_cost_rep
    extra_acc_dsp = "${:,.2f}".format(extra_acc)
    tot_acc += tot_prem
    tot_acc_dsp = "${:,.2f}".format(tot_acc)

# Report Footer

print("===========================================================")
print("Total policies: {}          {:>10} {:>10} {:>10}".format(pol_ctr, prem_acc_dsp, extra_acc_dsp, tot_acc_dsp))

# Report divider

print()
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("                      NEXT REPORT")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print()

# Report Title
print("ONE STOP INSURANCE COMPANY")
print("MONTHLY PAYMENT LISTING AS OF {}".format(pol_date_dsp))
print()

# Report Heading
print("POLICY   CUSTOMER           TOTAL                 TOTAL      MONTHLY")
print("NUMBER   NAME              PREMIUM       HST      COST       PAYMENT")
print("=====================================================================")

# Report Contents

scd_pol_ctr = 0     # Number of policies for second(scd) report
scd_pol_ctr_dsp = ""
scd_tot_acc = 0     # Sum of Total Premiums for second(scd) report
scd_tot_acc_dsp = ""
hst_acc = 0         # Sum of HST
hst_acc_dsp = ""
cost_acc = 0        # Sum of Total Cost
cost_acc_dsp = ""
mon_acc = 0         # Sum of Monthly Payments
mon_acc_dsp = ""

f = open("Policies.dat", "r")

for line in f:
    data_obj = line.split(",")
    pol_num_scd_rep = data_obj[0].strip()
    cus_name_scd_rep = "{} {}".format(data_obj[1].strip(), data_obj[2].strip())
    ins_prem_scd_rep = float(data_obj[13].strip())

    extra_cost_scd_rep = 0
    if data_obj[9].strip() == "Y":
        extra_cost_scd_rep += EXTRA_LIA_COST
    if data_obj[10].strip() == "Y":
        extra_cost_scd_rep += GLASS_COV_COST
    if data_obj[11].strip() == "Y":
        extra_cost_scd_rep += LOAN_CAR_COV_COST

    tot_prem_scd_rep = ins_prem_scd_rep + extra_cost_scd_rep
    tot_prem_scd_rep_dsp = "${:,.2f}".format(tot_prem_scd_rep)
    hst_rep = tot_prem_scd_rep * HST_RATE
    hst_rep_dsp = "${:,.2f}".format(hst_rep)
    total_cost = tot_prem_scd_rep + hst_rep
    total_cost_dsp = "${:,.2f}".format(total_cost)
    mon_pay_rep = (total_cost + PROC_FEE_RATE) / 12
    mon_pay_rep_dsp = "${:,.2f}".format(mon_pay_rep)

    if data_obj[12].strip() == "M":
        print("{}  {:<20} {:>9}    {:>7}  {:>9}  {:>9}".format(pol_num_scd_rep, cus_name_scd_rep, tot_prem_scd_rep_dsp, hst_rep_dsp, total_cost_dsp, mon_pay_rep_dsp))

        scd_pol_ctr += 1
        scd_tot_acc += tot_prem_scd_rep
        scd_tot_acc_dsp = "${:,.2f}".format(scd_tot_acc)
        hst_acc += hst_rep
        hst_acc_dsp = "${:,.2f}".format(hst_acc)
        cost_acc += total_cost
        cost_acc_dsp = "${:,.2f}".format(cost_acc)
        mon_acc += mon_pay_rep
        mon_acc_dsp = "${:,.2f}".format(mon_acc)


# Report Footer

print("=====================================================================")
print("Total policies: {}         {:>10} {:>10} {:>10} {:>10}".format(scd_pol_ctr, scd_tot_acc_dsp, hst_acc_dsp, cost_acc_dsp, mon_acc_dsp))
