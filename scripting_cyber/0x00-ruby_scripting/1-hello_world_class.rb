#!/usr/bin/env ruby


class HelloWorld
  def initialize
    set_message
  end

  def set_message
    @message = "Hello, World!"
  end

  def print_hello
    puts @message
  end
end

