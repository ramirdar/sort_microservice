# sort_microservice

Clear instructions for how to REQUEST data from the microservice you implemented. Include an example call.

To request data, you need to enter a dict type into the checklist json file. What will be sorted is the keys inside the dict. 
Ex: dict = {
    "do homework": "",
    "school": "",
    "take shower": ""
  }
    file = open('sort_file.json','w+')
    file.write(dict)
    file.close()
    
    Then run the sort.py program
  
 
  
Clear instructions for how to RECEIVE data from the microservice you implemented

Once the tasks are sorted and numbered, they will be sent to sort_file.json as a string dictonary type where the task is the key and the value will be the rank. To access this, you need to pass the data contents from sort_file.json into your program.

UML sequence diagram showing how requesting and receiving data work. Make it detailed enough that your partner (and your grader) will understand


https://lucid.app/lucidchart/5f5d39d5-51da-4c89-ba2f-60ea67ca4727/edit?invitationId=inv_37f330c3-ca5e-4fe8-9e77-00d454c91b99
