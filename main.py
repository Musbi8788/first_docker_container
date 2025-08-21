"""A simple program that chat with you"""
print("Type 'q' to exit")
run_time = 5
while True:
    print(f"Running time: {run_time}")
    run_time -= 1
    if run_time < 0:
        break
    try:
        
        name = input("\nWhat's your name? ")
        if name == 'q':
            break
    except EOFError:
        name = "musbi"

    
    try:
        feeling = input(f"\nHello {name}, How are you doing? ")
        if feeling == 'q':
            break
        
    except EOFError:
        feeling = "fine"
        print(f"You are {feeling}, Thanks...")
    else:
        print(f"You are {feeling}, Thanks...")
    
