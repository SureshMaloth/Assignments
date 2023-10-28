"""Q.Write a program to build a simple hospital management system 
using Python which can perform the following operations: 
1.write a method to takes details from the patient then store.
2.write a method to display all the details of patients.
3.write a method to search particular patient from the list.
 search by ID 
4.write a method to delete a particular patient details by ID.
5.write a method to update a selected patient details by ID.     

use list, dictionary to store data"""



class HospitalManagement:
    
    def __init__(self):
        
        self.addpatientList={}

        self.patientDetails()
    def patientDetails(self):
        user_input=input("""Please Select the Method With Num From 1 t0 5
                         1 gives addpatient()
                         2 gives patientProfile()
                         3 gives particularPatient()
                         4 gives removePatient()
                         5 gives updatePatient() :""")
        if user_input=="1":
            self.addPatient()
        elif user_input=="2":
            self.patientProfile()
        elif user_input=="3":
            self.particularPatient()
        elif user_input=="4":
            self.removePatient()
        elif user_input=="5":
            self.updatePatient()
    
    def addPatient(self):
        
        for i in range(int(input("enter the How Many patient Are There:"))):
            self.name=input("enter the Patient name:")
            self.id=int(input("enter the Patient id:"))
            self.address=input("enter the Patient  address:")
            self.patientNo=int(input("enter the patient No:"))
            PatientList={"Name":self.name,"id":self.id,"address":self.address}
            self.addpatientList[self.patientNo]=PatientList
            print(self.addpatientList)
    def patientProfile(self):
        self.addPatient()
        for i in (self.addpatientList.values()):
            print(i)
    def particularPatient(self):
        nbr=int(input("Enter The Number which Pateint Details Do You Want :"))
        self.addPatient()
        if nbr in self.addpatientList:
            
            print(self.addpatientList[nbr])
        else:
            print("Enter the wrong Nbr")
    def removePatient(self):
        nbr=int(input("Enter the Remove particular Pateint Num:"))
        self.addPatient()
        if nbr in self.addpatientList:
            
            (self.addpatientList.pop(nbr))
            print(self.addpatientList)
        else:
            print("Enter the wrong Nbr")
    def updatePatient(self):
        nbr=int(input("enter the Update particular Pateint Num:"))
        given_key=input("enter the key:")
        update_value=input("enter the val:")
        self.addPatient()
        if nbr in self.addpatientList:
            self.addpatientList[nbr][given_key]=update_value
            print(self.addpatientList)
        else:
            print("Enter the wrong Nbr")


            
        

        
        
        
HospitalManagement()
  
  
