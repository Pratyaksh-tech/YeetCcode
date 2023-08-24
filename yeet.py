import pandas as pd
import os

data = {'Name' : [], 'Age' : [], "Net Worth" : [], "Nationality" : []};

if os.path.exists('stuff.csv'):
	df = pd.read_csv('stuff.csv');
else: df = pd.DataFrame();

def add_stuff():
	global df
	name = input("Enter the name of the Billionaire: ");
	age = int(input(f"Enter the age of {name}: "))
	net_worth = input(f"Enter how much $$ {name} got: ");
	nationality = input(f"{name} Nationality: ");
	data['Name'].append(name); data['Age'].append(age); data['Net Worth'].append(net_worth); data['Nationality'].append(nationality);
	df = pd.DataFrame(data);
	df.to_csv('stuff.csv');
	print('\n');
	print("Operation Successful..."); print('\n');

def view_stuff(para = False):
	global df
	nm = input("Enter the name of the Billionaire you wanna view: ");
	rc = df.loc[df['Name'] == nm]
	if para:
		print(f"The name of the Billionaire is {nm} and his age is {rc['Age'].values[0]}. He is from {rc['Nationality'].values[0]} and his Net Worth is {rc['Net Worth'].values[0]}")
		return;
	print(rc);

def update_stuff():
	nm = input("Enter the name you want to update the details of. ");
	age = int(input(f"Enter the updated age of {nm} : "));
	nw = input(f"Enter the updated Net Worth of {nm} : ");
	nation = input(f"Enter the updated Nationality of {nm} : ");
	
	df.loc[df['Name'] == nm, 'Age'] = age;
	df.loc[df['Name'] == nm, 'Net Worth'] = nw;
	df.loc[df['Name'] == nm, 'Nationality'] = nation;
	df.to_csv('stuff.csv');
	print('\n'); print("Operation Successful.."); print('\n');

cd = None;
while(cd != 0):
	print('\n');
	print(f"Press 1 to add a record.")
	print(f"Press 2 to view a record.")
	print(f"Press 3 to view the entire Data file.")
	print(f"Press 4 to update a specific record.")
	print(f"Press 5 to delete a record.")
	print(f"SPECIAL, Press 6 to view the data of a specific Billionaire in a paragraph. ");
	print('\n');

	print('\n');
	cd = int(input("Enter some Juicy commands: "));
	if(cd == 1): 
		add_stuff();
	elif(cd == 2):
		view_stuff();
	elif(cd == 3):
		print(df);
	elif(cd == 4):
		update_stuff();
	elif(cd == 5):
		print('\n');
		nm = input("Enter the name you want to yeet: ");
		df = df.loc[df['Name'] != nm];
		print('\n'); print("Succefully Removed the Record...")
	elif(cd == 6):
		view_stuff(True);
	elif cd == 0: pass;
	else: print("Invalid Code.. Try again Bitch");
