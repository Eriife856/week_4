from pathlib import Path
workspace= Path("participants")
workspace.mkdir(exist_ok=True)
Path=workspace/"contact.csv"

#collects participant details
while True:
  name= input("Kindly input your name: ")

  try:
     age = int(input("Kindly input your age: "))
     if age > 5:
       break
     else:
       print("age must be greater than five: ")
       continue
  except ValueError:
       print("enter only number greater than five: ")
       
  track= input("Kinldy input your track: ")

  phone_number= (input("kindly in put your phone number: "))
  if len(phone_number)!= 11: 
    break
    print("invalid number.enter a valid number: ")
    continue
  else:
    print("enter valid number: ")

  break
with open(csv_file,"a", newline="") as file:
   writer= csv_Dictwriter(file, filenames= ["name","age","track","phone_number"])
   writer.writerrow({
    "name": name,
    "age": age,
    "track": track,
    "phone_number": phone_number,
})
print("participant valid details saved successfully!")

another_entry = input("do you want to register another participant? yes/no:").strip().lower()
if another_entry!="yes":
   print("Thank you.") 
   