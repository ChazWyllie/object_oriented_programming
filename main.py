import car

def main():
    
    carList = []
    while True:
        print("1. Create a car object")
        print("2. Display the details of the car")
        print("3. Display the details of all the cars")
        print("4. Delete a car object")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            newCar = car.Car()
            newCar.setBrand(input("Enter the brand of the car: "))
            newCar.setModel(input("Enter the model of the car: "))
            newCar.setYear(input("Enter the year of the car: "))
            newCar.setColor(input("Enter the color of the car: "))
            carList.append(newCar)
        elif choice == 2:
            i = int(input("Enter the index of the car: "))
            carList[i].display()
        elif choice ==3:
            for i in range(len(carList)):
                print("Car ", i)
                carList[i].display()
        elif choice == 4:
            i = int(input("Enter the index of the car: "))
            carList.pop(i)
        elif choice == 5:
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()