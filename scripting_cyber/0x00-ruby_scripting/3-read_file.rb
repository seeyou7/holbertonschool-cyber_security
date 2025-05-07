# Load the JSON module to work with JSON data
require 'json'

# Define a function named 'count_user_ids' that takes a file path as input
def count_user_ids(path)
    
    # Read the entire content of the file located at the given path
    file_content = File.read(path)
    
    # Parse the file content from JSON format into a Ruby data structure (usually an array of hashes)
    data = JSON.parse(file_content)

    # Create a new hash with a default value of 0 to count how many times each userId appears
    user_id_counts = Hash.new(0)

    # Loop through each item (hash) in the parsed data array
    data.each do |entry|
        # Extract the value associated with the key 'userId' from the current entry
        user_id = entry['userId']
        
        # Increment the count for this specific userId by 1
        user_id_counts[user_id] += 1
    end

    # Sort the hash by userId (key), then loop through each userId and its count
    user_id_counts.sort.each do |user_id, count|
        # Print the userId and the number of times it appeared in the JSON file
        puts "#{user_id}: #{count}"
    end

end

