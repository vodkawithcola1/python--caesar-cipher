import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shifted_message  = []

is_finished = False

print(art.logo)

while not is_finished:
    decision = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").replace(" ","")
    message = input("Type your message: ").lower()
    shift_number = int(input("Type the shift number: "))

    match decision:
        case "encode":
            for i in message:
                for j in alphabet:
                    if i == j:
                        alphabet_index = alphabet.index(j)
                        alphabet_index += shift_number
                        if alphabet_index > len(alphabet) - 1:
                            alphabet_index %= len(alphabet)
                            shifted_message.append(alphabet[alphabet_index])
                        else:
                            shifted_message.append(alphabet[alphabet_index])
                    elif i == " ":
                        shifted_message.append(" ")
                        break
            print(f"Here's the encoded result: {"".join(shifted_message)}")
            shifted_message.clear()

        case "decode":
            for i in message:
                for j in alphabet:
                    if i == j:
                        alphabet_index = alphabet.index(j)
                        alphabet_index -= shift_number
                        if alphabet_index > len(alphabet) - 1:
                            alphabet_index %= len(alphabet)
                            shifted_message.append(alphabet[alphabet_index])
                        else:
                            shifted_message.append(alphabet[alphabet_index])
                    elif i == " ":
                        shifted_message.append(" ")
                        break

            print(f"Here's the decoded result: {"".join(shifted_message)}")
            shifted_message.clear()
    finish = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    print("")
    if finish == "no":
        is_finished = True
        print("Thank you for using the program :)")