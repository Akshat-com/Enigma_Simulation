!pip install py-enigma

from enigma.machine import EnigmaMachine
import re

# Set up the Enigma machine
machine = EnigmaMachine.from_key_sheet(
    rotors='I II III',           # Rotor order
    reflector='B',               # Standard WWII reflector
    ring_settings='A B D',       # Ring settings
    plugboard_settings=''        # No plugboard used
)

# Set initial rotor positions
machine.set_display('XYW')

# Your plaintext
plaintext = "India walks out of Indus Water Treaty, endangering Pak's share of Indus River and it's tributries."

# Clean the text (remove punctuation and convert to uppercase)
clean_plaintext = re.sub(r'[^A-Z]', '', plaintext.upper())

# Encipher the cleaned plaintext
ciphertext = machine.process_text(clean_plaintext)

# Output the result
print("Ciphertext:", ciphertext)

print("Plaintext:", clean_plaintext)

if len(str(clean_plaintext)) == len(str(ciphertext)) :
    print("True")

# decipher the cleaned plaintext
deciphertext = machine.process_text(ciphertext)

# decipher the cleaned plaintext

# Set initial rotor positions for deciphering
machine.set_display('XYW')

deciphertext = machine.process_text(ciphertext)

print("Deciphertext:", deciphertext)

if deciphertext == clean_plaintext :
    print("True")

