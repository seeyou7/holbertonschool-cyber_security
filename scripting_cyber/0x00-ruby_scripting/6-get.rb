require 'net/http'
require 'uri'
require 'json'

def get_request(url)
  # Parse the URL
  uri = URI.parse(url)
  
  # Perform the GET request
  response = Net::HTTP.get_response(uri)
  
  # Print the response status
  puts "Response status: #{response.code} #{response.message}"
  
  # Parse and pretty-print the JSON response body
  if response.body
    json_body = JSON.parse(response.body)
    puts "Response body:"
    puts JSON.pretty_generate(json_body)
  end
end

