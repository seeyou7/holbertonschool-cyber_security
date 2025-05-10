class CaesarCipher
    def initialize(shift)
      @shift = shift
    end
  
    def encrypt(message)
      cipher(message, @shift)
    end
  
    def decrypt(message)
      cipher(message, -@shift)
    end
  
    private
  
    def cipher(message, shift)
      message.chars.map do |char|
        if char.match?(/[A-Za-z]/) # Check if the character is a letter
          base = char.ord < 91 ? 'A'.ord : 'a'.ord
          (((char.ord - base + shift) % 26) + base).chr
        else
          char # Non-alphabetic characters remain unchanged
        end
      end.join
    end
  end
