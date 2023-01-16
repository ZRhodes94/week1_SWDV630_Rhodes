class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)

    def __contains__(self, substring):
        if substring in self.__myTeam:
            return True
        else:
            return False

    def __iter__(self):
        self.c = 0
        return self
    
    def __next__(self):
        if self.c < len(self.__myTeam):
            x = self.c
            self.c += 1
            return self.__myTeam[x]
        else:
            raise StopIteration

def main():
    classmates = Teams(['John', 'Steve', 'Tim'])

    #Checks if Tim and Sam are in the team
    print('Tim' in classmates)
    print('Sam' in classmates)

    #Iterates through team list
    for member in classmates:
        print(member)

    #Prints the len of classmates- this class does implement the __len__ method
    print (len(classmates))

main()