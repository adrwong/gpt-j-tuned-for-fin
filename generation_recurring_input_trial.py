from transformers import AutoModelForCausalLM, AutoTokenizer
import sys

model = AutoModelForCausalLM.from_pretrained("../tuned_to_finbase_3_slim_hf")
tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-j-6B', local_files_only=True)

# tokenizer = GPT2Tokenizer.from_pretrained('EleutherAI/gpt-j-6B')
# model = GPTJModel.from_pretrained('../../tuned_to_finbase2_slim_hf', local_files_only=True)


input_ids = tokenizer("Hello, my dog is cute", return_tensors="pt").input_ids

gen_tokens = model.generate(input_ids, do_sample=True, temperature=0.9, max_length=100,)
gen_text = tokenizer.batch_decode(gen_tokens)[0]

print(gen_text)
 
print("Exit")
