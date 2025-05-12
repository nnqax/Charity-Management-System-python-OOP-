# Charity-Management-System-python-OOP-
Welcome to the Charity Management System! This simple system helps charities keep track of their important work: who they help, who donates, and how aid is distributed.

What Does This System Do?
This system is designed to help charities manage their day-to-day operations by:

Keeping track of people who need help (Beneficiaries): Records their names, what they need, and their financial situation.
Recording donations: Logs gifts from supporters, whether it's money or items like clothes.
Managing generous givers (Donors): Keeps a record of who donates and their donation history.
Overseeing assistance programs: Helps define what kind of aid is available and who qualifies for it.
Allocating aid: Makes sure the right help gets to the right people, based on eligibility rules.
How to Use It (Getting Started)
This system is currently a basic Python program you run from your computer's command line.

To use it:

Save the Code: Copy all the provided Python code into a file. You can name it something like charity_system.py.
Open a Terminal/Command Prompt:
On Windows: Search for "Command Prompt" or "PowerShell."
On Mac/Linux: Open the "Terminal" application.
Navigate to the Folder: Use the cd command to go to the folder where you saved your charity_system.py file.
Example: If your file is in a folder called MyCharityApp on your Desktop, you might type: cd Desktop/MyCharityApp
Run the Program: Once in the correct folder, type:
Bash

python charity_system.py
Interact with the Menu: The program will then display a menu in your terminal. You can choose options by typing the corresponding number and pressing Enter.
Main Features Explained
Let's break down the core functions of this system:

1. Beneficiary Management
Add Beneficiary: Add new individuals or families who need assistance. You'll record their name, what kind of help they require (e.g., "food," "shelter," "medical"), and their income level.
Record Assistance: When a beneficiary receives help, you can add that to their record so you know what they've received over time.
View Beneficiaries: See a list of all the people currently registered to receive help, along with their needs and what aid they've been given.
2. Donation Management
Record Donation: Log new donations. You'll specify the donor, whether it's a "monetary" (cash) donation with an amount, or a "non-cash" donation (like clothes, food, or supplies) with a description.
View Donations: See a list of all recorded donations, including who gave what, when, and the type of donation.
3. Donor Management
Add Donor: Register new individuals or organizations who wish to donate.
Track Donor Contributions: The system keeps a history of all donations made by each donor.
Get Total Monetary Donations: Quickly see the total amount of money a specific donor has contributed.
View Donors: See a list of all registered donors and their contact information.
4. Assistance Programs
Add Program: Define different types of assistance programs your charity offers (e.g., "Emergency Food Aid," "Medical Support," "Educational Grants"). For each program, you'll set eligibility rules (e.g., "income less than $X") and what types of aid it provides.
Check Eligibility: The system helps determine if a beneficiary qualifies for a specific program based on your defined criteria.
Allocate Aid: Distribute aid to eligible beneficiaries through a specific program. This process automatically updates the beneficiary's records.
View Programs: See a list of all your charity's assistance programs, their descriptions, eligibility criteria, and the types of aid they offer.
Important Notes
Data Storage: Currently, this system does not save your data when you close the program. If you close the terminal window, all the information you entered will be lost. For a real-world system, you would need to add features to save data to a file or a database.
Eligibility Criteria: The eligibility check is currently based on Beneficiary.income <= self.eligibility_criteria. In a real system, this logic would be much more detailed, checking various factors like needs, family size, location, etc.
Error Handling: While there's some basic checking (like making sure monetary donations have an amount), a more robust system would have more comprehensive error management and user input validation.
No Advanced Features: This is a foundational system. It doesn't include features like user authentication (login/passwords), detailed reporting, or a graphical user interface (GUI).
