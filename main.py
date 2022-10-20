movies = [ "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
            ["Graham Chapman",
                [ "Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]


for i in movies:
    print (i)
    
    isinstance(movies,list)
    True
    num_names = len(movies)
    isinstance (num_names,list)
    
    #The inner list within the inner list is printed “as-is.”
    
    #any list item can itself be another list:
    #any list item can itself be another list:
         #print(movies[4][1][3])
         
    #for (target identifier)  in (list)  :
          #{list processing code}
          
          #checking list with if else statements
              #if (some condition holds):
                  #(run the true suite)
              #else:
                  #(run the false suite)
                  
                  
#No surprises here, as the if statement in Python works pretty much as
#expected. But what condition do you need to check? You need a way to
#determine if the item currently being processed is a list. Luckily, Python ships
#with a BIF that can help here: isinstance()    

#What’s cool about the isinstance() BIF is that it lets you check if a
#specific identifier holds data of a specific type