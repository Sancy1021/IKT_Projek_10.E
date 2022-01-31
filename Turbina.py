turbine_counter= 1
all_turbines= 25
turbine_power= 2000
total_power= 0

while turbine_counter <= all_turbines:
    print(turbine_counter)
    turbine_counter +=1
    if turbine_counter <11:
        total_power = turbine_counter * turbine_power
        print(f'A(z) {turbine_counter}.számú szélturbina teljes fordulaton müködik, 2000 MWh-t termelve. \n A farmon termel összenergia jelenleeg 2000MWh-t termel')
    elif turbine_counter < 21:
        total_power = turbine_counter * turbine_power/2
        print(f'A(z) {turbine_counter}.számú szélturbina fél fordulaton müködik, 1000 MWh-t termelve. \n A farmon termel összenergia jelenleeg 1000MWh-t termel')
    else:
        print(f"A(z) {turbine_counter}.számú szélturbina egyhelyben áll fordulaton müködik, 0 MWh-t termelve. \n A farmon termel összenergia jelenleeg 0MWh-t termel")
    
    turbine_counter += 1 
