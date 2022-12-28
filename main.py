import time

sentences = [
    "Five little monkeys jumping on the bed.",
    "One fell off and bumped his head.",
    "Mama called the doctor and the doctor said, no more monkeys jumping on the bed!"
]

total_time = 0

for sentence in sentences:
    # Display the sentence
    print(sentence)

    # Start the timer
    start_time = time.time()

    # Get the user's input
    user_input = input("Type the sentence:\n")

    # Stop the timer
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Add the elapsed time to the total time
    total_time += elapsed_time

    # Calculate the accuracy of the user's input
    accuracy = 100 * (len(sentence) - abs(len(sentence) - len(user_input))) / len(sentence)

    # Print the accuracy
    print(f"Accuracy: {accuracy:.2f}%")

    # Add empty row
    print()

# Print the total time
print(f"Total time: {total_time:.2f} seconds")
