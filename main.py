from pet import Pet

def main():
    # Create a pet named Denzel as requested
    my_pet = Pet("Denzel")
    
    print(f"Welcome to Digital Pet! Meet your new pet, {my_pet.name}!")
    
    # Test the basic functionality
    my_pet.get_status()
    
    # Let's play with Denzel
    my_pet.play()
    my_pet.get_status()
    
    # Denzel is getting hungry
    my_pet.eat()
    my_pet.get_status()
    
    # Denzel is tired after playing and eating
    my_pet.sleep()
    my_pet.get_status()
    
    # Bonus features - teach some tricks
    my_pet.train("sit")
    my_pet.train("roll over")
    my_pet.train("fetch")
    my_pet.show_tricks()
    
    # Check status after training
    my_pet.get_status()

if __name__ == "__main__":
    main()