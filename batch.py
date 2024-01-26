def get_next_batch_name(previous_batch):
    # Extract the components of the previous batch
    year, month, day, hour, minute = map(int, previous_batch.split('_'))

    # Increment the minute
    minute += 1

    # Adjust hour and minute if necessary
    if minute > 11:
        minute = 0
        hour += 1

    if hour > 23:
        hour = 0
        # If you want to roll over to the next day, update day, month, and year as well

    # Format the components into the batch name
    next_batch = f"{year:04}{month:02}{day:02}_{hour:02}_{minute:02}"

    return next_batch


def generate_triggered_batches():
    # Ask the user for input lists
    list1 = input("Enter the first list of batches (comma-separated): ").split(',')
    list2 = input("Enter the second list of batches (comma-separated): ").split(',')
    
    # Combine the two lists
    triggered_batches = list1 + list2
    
    # Sort the combined list
    triggered_batches.sort()
    
    return triggered_batches

for i in range(len(triggered_batches)-1):
    current_batch = triggered_batches[i]
    next_batch = triggered_batches[i+1]
    
    current_time = datetime.strptime(current_batch, "%Y%m%d_%H_%M")
    next_time = datetime.strptime(next_batch, "%Y%m%d_%H_%M")

    while current_time + timedelta(minutes=5) < next_time:
        unprocessed_batch = current_time + timedelta(minutes=5)
        print(f"The batch {unprocessed_batch.strftime('%Y%m%d_%H_%M')} is unprocessed.")
        current_time = unprocessed_batch
