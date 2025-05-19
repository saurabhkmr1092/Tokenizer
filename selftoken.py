import string 
english_chars = list(string.ascii_letters)
hindi_chars = [chr(cp) for cp in range(0x0900, 0x097F + 1) if chr(cp) != ' ']
combined_chars = english_chars + hindi_chars
combined_chars.append(' ')
special_tokens = {
    "<PAD>": 0,
    "<START>": 1,
    "<END>": 2
}


vocab = special_tokens.copy()
for idx, char in enumerate(combined_chars, start=len(special_tokens)):
    vocab[char] = idx



def encode(text, vocab, add_special_tokens=True):
    token_ids = [vocab[char] for char in text]
    if add_special_tokens:
        token_ids = [vocab["<START>"]] + token_ids + [vocab["<END>"]]
    return token_ids



def decode(token_ids,vocab,remove_special_tokens=True):
    id_to_char = {idx: char for char, idx in vocab.items()}
    decoded_chars = []
    for token_id in token_ids:
        char = id_to_char.get(token_id, '') 
        if remove_special_tokens and char in ["<PAD>", "<START>", "<END>"]:
            continue
        decoded_chars.append(char)  
    return ''.join(decoded_chars)  



user_input = input("Enter your message (English or Hindi): ")
encoded_tokens = encode(user_input,vocab)
print("Encoded Token IDs:", encoded_tokens)

decoded_text = decode(encoded_tokens,vocab)
print("Decoded Message:", decoded_text)


user_input_decode = input("write tokens to decode")
token_ids = list(map(int, user_input_decode.strip().split()))
decoded_text = decode(token_ids,vocab)
print("Decoded Message:", decoded_text)