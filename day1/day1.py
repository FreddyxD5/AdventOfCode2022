elf_max_calories = 0
elf_calories = 0

with open('input.txt', 'r') as myfile:            
    for line in myfile.readlines():            
        if line.strip() =='':            
            if elf_calories > elf_max_calories:
                elf_max_calories = elf_calories
            elf_calories = 0
        else:            
            elf_calories += int(line)
                      
    
print(elf_max_calories)