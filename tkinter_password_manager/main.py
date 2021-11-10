from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR 
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_numbers = [random.choice(numbers) for num in range(nr_numbers)]
    password_symbols =[random.choice(symbols) for symbol in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password =''.join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear_entry_fields(): #delete the populated columns so new data can be added 
    website_entry.delete(0,END)
    # email_entry.delete(0,END) optional as we want to keep the same email
    password_entry.delete(0,END)
def capture_data(): #get data once the button is pressed 
    
    website = website_entry.get()
    email =email_entry.get()
    password =password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
                
    }

    #validation for empty entry fields
    if len(website)== 0 or len(password) ==0:
        messagebox.showerror(title='Error', message='1 or more fields are blank')
    else:

    #validation for empty entry fields

        #validation popup box before saving
        confirmation =messagebox.askokcancel(title='confirmation', message=f'the password for website {website} is: \n {password} \n Do you wish to save? ')
        if confirmation:
            #3 step process for saving data to JSON 
            #adding data to JSON file - read the file 1st / add new data ( with update ) and dump to save
            try:
                with open('password.json', mode='r') as file: 
                
                    #read the old data
                    json_data = json.load(file)
                    
                    #update old data with new data 
                    json_data.update(new_data)
                    
                #save (OVERWRITE) updated data (new_data_gets_saved_to, old_data, indent_no)
                with open ('password.json', mode='w') as file:
                    json.dump(json_data, file, indent=4)
            
            #error exception , password.json does not exist yet or has been deleted
            except FileNotFoundError:
                with open('password.json', mode='w') as file:
                    json.dump(new_data, file, indent=4)
                    
                    
            messagebox.showinfo("message", "password saved") #generate a confirmation popup box that the passowrd was saved 
            clear_entry_fields()
        else:
            messagebox.showinfo('messgae', message='password not saved ')


#-----------------------------------FIND PASSWORD-----------------------------
#search button functionality
#search and bring up existing records , if nothing is found , popup message to come up saying no records had been fond 
#tip data from JSON is jsut dict data 
def find_passoword():
    website = website_entry.get()
    try:
        
        with open('password.json', 'r') as data: 
            json_data = json.load(data)  
            # print(json_data)  #SANITY CHECK
    except FileNotFoundError:
        messagebox.showwarning(title= 'error', message='no Data file found')
    else:
        if website in json_data:
            email =json_data[website]['email']
            password =json_data[website]['password']
            messagebox.showinfo(title=website, message=f'Email {email},\n  password {password}')
            
        else: # catch out cases where the website has not been registered
            messagebox.showwarning(title= 'error', message='this website has not been registered')


# ---------------------------- UI SETUP 

window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200,  highlightthickness=0)
padlock_img= PhotoImage(file='logo.png') #image object needs to be first created before it is used in canvas .


#create_image method
canvas.create_image(100,100, image=padlock_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text='Website')
website_label.grid(column=0, row=1)

username_label = Label(text='Username/Email')
username_label.grid(column=0, row=2)

password_label = Label(text='password')
password_label.grid(column=0, row=3)


#entry fields
website_entry= Entry(width=17)
website_entry.focus() #puts the cursor in the entry field
#need a get method
website_entry.grid(column=1, row=1)

email_entry = Entry(width=35)
email_entry.insert(0, 'rafafilm01@hotmail.com') #pre-populates the entry field , END as the alternative index number
#need a get method
email_entry.grid(column=1, row=2 , columnspan=2)

password_entry = Entry(width=17)
password_entry.grid(column= 1,row=3 )


#buttons
generate_password_button = Button(text='Generate password', command=generate_password) 
generate_password_button.grid(column=2, row=3)

search_button = Button(text='Search', command=find_passoword, width=13)
search_button.grid(column=2, row=1)

get_button =Button(text='Add', width=30, command=capture_data) 
get_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
# ------------------------------- #