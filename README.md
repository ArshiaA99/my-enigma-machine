# 🔐 Enigma Machine Simulation in Python

This project is a simple but creative simulation of the famous **Enigma Machine** — the encryption device used by Nazi Germany during World War II.  
It demonstrates how text can be encoded through multiple layers of rotor substitutions, a reflector, and dynamic rotor rotation — all implemented in pure Python.

---

## 🧠 What Is the Enigma Machine?

The **Enigma Machine** was an electromechanical cipher device.  
Messages were scrambled through several rotating wheels (called *rotors*) that substituted letters in complex, ever-changing ways. When the operator typed a letter:
1. Electrical current would pass through multiple rotors.
2. The signal would bounce off a *reflector*, ensuring reversibility (so encryption = decryption).
3. The rotors would then shift positions after each keypress, altering the cipher dynamically.

The result was an encryption system so sophisticated that it remained unbreakable for years — until the Allies cracked it with a combination of mathematics, codebreaking, and early computing.

---

## 💡 What Makes This Code Special

This implementation captures the **core behavior** of Enigma in a clean and fully readable Python script.

### Key Highlights
- **Custom alphabet**:  
  Includes the standard lowercase letters **plus the space character** — allowing the cipher to handle full sentences gracefully.
  
- **Three deterministic rotors**:  
  Each rotor is created by shuffling the alphabet with different random seeds (42, 43, 44).  
  This ensures reproducibility while maintaining uniqueness

- **Reflector function: A simple yet clever mirror mechanism**:
  Each letter is reflected through the other side of the alphabet (like how Enigma’s electrical signal was reversed back).

- **Dynamic rotor rotation**:
  After encrypting each character, the rotors rotate to change the substitution pattern dynamically — making the cipher state-dependent. The outer rotors rotate      less frequently, emulating Enigma’s cascading rotation mechanism.

- **Self-contained encryption loop**:
  Encrypts any given plaintext string, producing a final encoded message that changes with each run based on rotor states.

## How it works?
1. Initialize the alphabet and rotors
2. Pass each character through 3 rotor layers
3. Apply reflector symmetry
4. Reverse the signal through rotors
5. Rotate rotors after each encryption step
6. Print the resulting cipher text

Note: Because of the reflector’s symmetry, running the cipher again with the same rotor setup will decode the message back to the original text.

Credits: Created by Arshia K ([Github: ArshiaA99](https://github.com/ArshiaA99))
