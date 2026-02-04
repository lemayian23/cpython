SIZE = 4 #Define the size of the hash table
class DataItem:
    def __init__(self,key):
        self.key = key

hashArray = [None] * SIZE #Define the hash table as a list of DataItem pointers

def hashCode(key):
    #Return a hash value based on the key
    return key % SIZE

def insert(key):
    # Create a new DataItem
    newItem = DataItem(key)
    #Initialize other data members if needed
    #Calculate the hash index for the key
    hashIndex = hashCode(key)


    #Handle collisions (linear probing)
    for _ in range(SIZE): #Loop at most SIZE times to avoid infinite loops
        if hashArray[hashIndex] == None:
            #Insert the new DataItem at the calculated index
            hashArray[hashIndex] = newItem
            return
        else:
            #Move to the next cell
            hashIndex = (hashIndex+1) % SIZE
            # If the table is full
            print(f"Hash table is full! Cannot insert key: {key}")

#  populate the hash table
insert(22)
insert(42)
insert(52)
insert(62)
insert(22)

#Display the hash table
for i, item in enumerate(hashArray):
    if item is not None:
        print(f"Index{i}:{item.key}")
    else:
        print(f"Index{i}:Empty")
