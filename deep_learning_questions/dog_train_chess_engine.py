# Dog wants to use GPT2 to train a chess engine, and he wants to know how big a GPU it needs to train and inference.
# Given a list of decoder-only network, the number of layers (A), vocabulary size (A), number of max sequence length (A & B & C),
# batch size for both train and inference (B & C), embedding dimension (A), number of self-attention head (A), compute type (float or int) (B & C)
# which optimizer (SGD, Adam, etc) (B). Boolean of whether a KV cache (C) is included.

# Part A: calculate trainable parameters
# Part B: Training memory
# Part C: Inference memory

# Validate against GPT2, lLama 7B and 70B

# for all 4 models:
# max seq len = 1024
# vocab_size = 50257

# expected param counts
# 'gpt2':         dict(n_layer=12, n_head=12, n_embd=768, ffw=3072),  # 124M params
# 'gpt2-medium':  dict(n_layer=24, n_head=16, n_embd=1024, ffw=4096), # 350M params
# 'gpt2-large':   dict(n_layer=36, n_head=20, n_embd=1280, ffw=5120), # 774M params
# 'gpt2-xl':      dict(n_layer=48, n_head=25, n_embd=1600, ffw=6400), # 1558M params


def calculate_trainable_parameters(n_layer, vocab_size, max_seq, n_embd, n_head, ffw):
    wte = vocab_size * n_embd
    wpe = n_embd * max_seq
    self_attn = n_embd * (3 * n_embd // n_head) * n_head
    W_o = n_embd * n_embd
    mlp = (n_embd * ffw) * 2  # two layers
    return wte + wpe + n_layer * (self_attn + W_o + mlp)


# Define GPT-2 models
models = {
    "gpt2": dict(n_layer=12, n_head=12, n_embd=768, ffw=3072),  # 124M params
    "gpt2-medium": dict(n_layer=24, n_head=16, n_embd=1024, ffw=4096),  # 350M params
    "gpt2-large": dict(n_layer=36, n_head=20, n_embd=1280, ffw=5120),  # 774M params
    "gpt2-xl": dict(n_layer=48, n_head=25, n_embd=1600, ffw=6400),  # 1558M params
}

for model_name, params in models.items():
    trainable_params = calculate_trainable_parameters(
        params["n_layer"],
        50257,
        1024,
        params["n_embd"],
        params["n_head"],
        params["ffw"],
    )
    print(f"{model_name}: Trainable parameters = {trainable_params / 1e6:.2f}M")
