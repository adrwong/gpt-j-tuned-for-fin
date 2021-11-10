from transformers import GPT2Tokenizer, GPTJModel
import torch

# tokenizer = GPT2Tokenizer.from_pretrained('EleutherAI/gpt-j-6B')
# model = GPTJModel.from_pretrained('EleutherAI/gpt-j-6B')

tokenizer = GPT2Tokenizer.from_pretrained('EleutherAI/gpt-j-6B')
model = GPTJModel.from_pretrained('../../tuned_to_finbase2_slim_hf', local_files_only=True)

inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
outputs = model(**inputs)

last_hidden_states = outputs.last_hidden_state

print(outputs)