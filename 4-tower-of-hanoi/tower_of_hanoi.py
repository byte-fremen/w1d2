count = 0
def move(disks, source="A", target="C", spare="B"):
    global count
    if disks == 0:
        return count
    else:
        move(disks-1, source, spare, target)
        count +=1
        move(disks-1, spare, target, source)
    
    return count

print(move(3))

count = 0
print(move(4))


