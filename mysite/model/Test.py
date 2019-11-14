#import Person from Human
from Human import Person

# Instantiate the Person object
#p1 = Person("Name", 12, 40.0)
def main():
    sammy = Person("Xenia", 25, 81.0)
    #sammy.swim()
    #sammy.be_awesome()
    sammy.introduce()

if __name__ == "__main__":
    main()
# Access the instance attributes
#print("{} is {} and {} is {}.".format(
#    philo.name, philo.age, mikey.name, mikey.age))
