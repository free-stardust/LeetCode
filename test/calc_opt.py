def mha(seq_len, heads, dim):
    flops = 0

    d_dim = dim // heads

    qkv_flops = seq_len * (2 * dim - 1) * d_dim * heads * 3
    attn_flops = (seq_len * (2 * d_dim - 1) * seq_len + \
                 seq_len * (2 * seq_len - 1) * d_dim) * heads
    o_flops = seq_len * (2 * dim - 1) * dim

    flops = qkv_flops + attn_flops + o_flops

    return flops


def ffn(seq_len, dim, ffn_dim):
    flops = 0

    flops = seq_len * (2 * dim - 1) * ffn_dim + \
            seq_len * (2 * ffn_dim - 1) * dim

    return flops


seq_len = 2048
heads = 32
layers = 32
dim = 4096
ffn_dim = 4 * dim

mha_flops = mha(seq_len, heads, dim)
ffn_flops = ffn(seq_len, dim, ffn_dim)
print(f"mha flops: {mha_flops}, "
      f"ffn flops: {ffn_flops}, "
      f"rate: {mha_flops / ffn_flops:.6f}")
