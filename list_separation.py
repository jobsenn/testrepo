from email.errors import InvalidMultipartContentTransferEncodingDefect


names = ['Michael', 'Terry',['james',['john','mathew','mark'],'zebedee']]



for each_person in names:
    print (each_person)
    
    if isinstance(each_person,list):
         for nested_person in each_person:
             print (nested_person)
             
                if isinstance(nested_person):
                    for deeply_nested in nested_person:
                        print(deeply_nested)
                        
                else:print(nested_person)
    else:
       print(each_person)