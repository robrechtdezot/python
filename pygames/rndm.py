import time

name = "Wout", "Servaes", "Janssens", "Peters"  
start_time = time.time()
for i in range(len(name)):
    print(name[i])
    
    if name[i] == "Janssens":
        print("Janssens gevonden")
        continue
    else:
        print("Niet Janssens")
  

    # Your existing code here

    end_time = time.time()
    print(f"Runtime: {end_time - start_time} seconds")