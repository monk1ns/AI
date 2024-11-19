from transformers import GPT2LMHeadModel, GPT2Tokenizer


model_name = "gpt2"  
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

start_phrase = "Once upon a time in a faraway land..."

input_ids = tokenizer.encode(start_phrase, return_tensors="pt")


output = model.generate(
    input_ids,
    max_length=50, 
    num_return_sequences=1, 
    no_repeat_ngram_size=2,  
    temperature=0.7,  
    top_p=0.9,  
    top_k=50,  
)


generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print("Generated story in English:")
print(generated_text)
