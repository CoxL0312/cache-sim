# cache_sim.py
# Direct-mapped cache simulator for word-addressed memory
# Cache: total_size_words = 8, block_size_words = 4  --> 2 lines (indices 0,1)
# @author Lindsey Cox
# Date: 10/2/2025
# Written for an assignment for Computer Architecture class

TOTAL_SIZE = 8
BLOCK_SIZE = 4
ACCESS_SEQ = [30, 31, 32, 33, 30, 31, 34, 35, 40, 41, 32, 30, 40, 41, 50, 43, 44, 40, 41, 31]

# Derived
NUM_LINES = TOTAL_SIZE // BLOCK_SIZE  # = 2

# Each line holds either None or a block number (tag)
cache = [None] * NUM_LINES

def block_num(addr):     # which memory block this word lives in
    return addr // BLOCK_SIZE

def cache_index(block):  # which cache line for that block
    return block % NUM_LINES

def block_words(block):  # the 4-word range for this block
    start = block * BLOCK_SIZE
    return start, start + BLOCK_SIZE - 1

print(f"Direct-Mapped Cache  |  total={TOTAL_SIZE} words, block={BLOCK_SIZE} words")
print(f"Lines/indices: {NUM_LINES}  -> indices: {list(range(NUM_LINES))}\n")

for i, addr in enumerate(ACCESS_SEQ, 1):
    blk = block_num(addr)
    idx = cache_index(blk)
    start, end = block_words(blk)

    print(f"Access #{i}: memory address {addr}")
    print(f"  Memory block number = {addr} div {BLOCK_SIZE} = block {blk}")
    print(f"  Cache index for block {blk} = {blk} mod {NUM_LINES} = cache index {idx}")

    if cache[idx] == blk:
        print("  HIT – memory word is in the cache at index", idx)
    else:
        prev = cache[idx]
        if prev is None:
            print("  MISS – line empty at this index")
        else:
            p0, p1 = block_words(prev)
            print(f"  MISS – evict block {prev} (words {p0}-{p1}) from index {idx}")

        cache[idx] = blk
        print(f"  Load entire memory block {blk} (words {start}-{end}) into cache index {idx}")

    # Show tiny cache summary after each access
    def line_desc(tag):
        if tag is None: return "∅"
        s, e = block_words(tag)
        return f"blk {tag} [{s}-{e}]"
    print(f"  Cache now -> index 0: {line_desc(cache[0])} | index 1: {line_desc(cache[1])}\n")
