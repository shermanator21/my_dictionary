import csv

datastore = { "medical":[ 
         { "room-number": 100,
          "use": "reception",        
          "sq-ft": 50,        
          "price": 75      
        },      
        { "room-number": 101,        
         "use": "waiting",        
         "sq-ft": 250,        
        "price": 75      
        },      
        { "room-number": 102,        
        "use": "examination",        
        "sq-ft": 125,        
        "price": 150      
        },      
        { "room-number": 103,        
        "use": "examination",        
        "sq-ft": 125,        
        "price": 150      
        },      
        { "room-number": 104,        
        "use": "office",        
        "sq-ft": 150,        
        "price": 100      
        }   

        ]
 }


outfile = open('retail_space.csv', 'w')
outfile.write('room-number, use, sq-ft, price\n')

for l in datastore["medical"]:
    outfile.write(
        str(l["room-number"]) 
        + "," 
        + l["use"] 
        + "," 
        + str(l["sq-ft"])
        + "," 
        + str(l["price"])
        + "\n"
    )

outfile.close()

