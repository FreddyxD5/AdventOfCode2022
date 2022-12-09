

def top_tree_elf():
    elf_max_calories = 0
    elf_calories = 0
    elf_carrys = []
    with open('input.txt', 'r') as myfile:            
        for line in myfile.readlines():            
            if line.strip() =='':            
                elf_carrys.append(elf_calories)
                elf_calories = 0
            else:            
                elf_calories += int(line)
                        
    elf_carrys.sort()
    return elf_carrys[-3:]
print(top_tree_elf())