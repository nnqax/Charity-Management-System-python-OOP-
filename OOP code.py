
class Beneficiary: #initialize the class of the beneficiary

    def __init__(self, name, needs, income): #initialize the attributes to assign the beneficiary
        self.name = name #assigning the name attribute
        self.income = income #assigning the income attribute
        self.needs = needs #assigning the need attribute
        self.assistance = [] #making the assistance list for everything the beneficiary took

    def record_assistance(self, item):
        self.assistance.append(item) #inputs the items taken by the beeficiary in the list
        print(f"Recorded assistance '{item}' for {self.name}")
    def __str__(self):
        return f"Beneficiary: {self.name}, Needs: {self.needs}, Assistance: {self.assistance}"

class Donation: #initialize the class of the donation
    def __init__(self, donor, donation_type, amount=None, non_cash_description=None):
        self.donor = donor
        self.donation_type= donation_type.lower()
        self.amount = amount
        self.non_cash_description = non_cash_description

        if self.donation_type == 'monetary' and self.amount is None: #checking if the donation matches the type
            raise ValueError("Monetary donation must have an amount.")
        elif self.donation_type == 'non-cash' and self.non_cash_description is None:#checking if the donation matches the type
            raise ValueError("Non-cash donation must have a description.")

        donor.record_donation(self) # Automatically record the donation with the donor

    def __str__(self):
        if self.donation_type == 'monetary':
            return f" Donor: {self.donor.name}, Type: Monetary, Amount: ${self.amount}"
        else:
            return f" Donor: {self.donor.name}, Type: Non-Cash, Description: {self.non_cash_description}"

class Donor: #initialize the class of the donor

    def __init__(self, name):
        """
        Initializes a new Donor object.
        """
        self.name = name
        self.donations = []

    def record_donation(self, donation): #Records a donation made by the donor.
         self.donations.append(donation)

    def get_total_monetary_donations(self):#Calculates and returns the total monetary amount donated by the donor.

        total = 0
        for donation in self.donations:
            if donation.donation_type == 'monetary':
                total += donation.amount
        return total

    def __str__(self):
        return f"Name: {self.name}"


class AssistanceProgram: #Represents a program that provides assistance to beneficiaries.

    def __init__(self, name, eligibility_criteria, assistance_types):
        """
        Initializes a new AssistanceProgram object.
        """
        self.name = name
        self.eligibility_criteria = eligibility_criteria
        self.assistance_types = assistance_types

    def check_eligibility(self, beneficiary):  #Checks if a beneficiary is eligible for this program.

        print(f"Checking eligibility for {beneficiary.name} for program: {self.name}...")
        print(f"Eligibility Criteria: {self.eligibility_criteria}")

        if Beneficiary.income <= self.eligibility_criteria:
            print(f"The beneficiary is eligible for this Criteria: {self.eligibility_criteria}")
            return True
        else:
            print(f"The beneficiary is not eligible for this Criteria: {self.eligibility_criteria}")
            return False



    def allocate_aid(self, beneficiary, aid_type, description):
        """
        Allocates aid to a beneficiary under this program.
        """
        if aid_type not in self.assistance_types:
            print(f"Error: {aid_type} is not a valid aid type for {self.name}.")
            return

        if self.check_eligibility(beneficiary):
            beneficiary.add_assistance(aid_type, description)
            print(f"Aid allocated to {beneficiary.name} under {self.name}.")
        else:
            print(f"{beneficiary.name} is not eligible for {self.name}.")

    def __str__(self):
        return f" Name: {self.name}"

class CharitySystem:
    def __init__(self):
        self.beneficiaries = []
        self.donations = []
        self.donors = []
        self.programs = []

    def add_beneficiary(self, name, needs):
        beneficiary = Beneficiary(name, needs)
        self.beneficiaries.append(beneficiary)
        print(f"Added beneficiary: {beneficiary.name}")

    def add_donor(self, name):
        donor = Donor(name)
        self.donors.append(donor)
        print(f"Added donor: {donor.name}")
        return donor

    def record_donation(self, donor, item):
        donation = donor.make_donation(item)
        self.donations.append(donation)

    def add_program(self, name, criteria):
        program = AssistanceProgram(name, criteria)
        self.programs.append(program)
        print(f"Added program: {program.name}")
        return program

    def provide_aid(self, beneficiary, program, aid_item):
        program.provide_aid(beneficiary, aid_item)

    def list_beneficiaries(self):
        print("\n--- Beneficiaries ---")
        for b in self.beneficiaries:
            print(b)

    def list_donations(self):
        print("\n--- Donations ---")
        for d in self.donations:
            print(d)

    def list_donors(self):
        print("\n--- Donors ---")
        for dr in self.donors:
            print(dr)

    def list_programs(self):
        print("\n--- Assistance Programs ---")
        for p in self.programs:
            print(p)

