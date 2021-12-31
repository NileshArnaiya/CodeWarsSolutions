# You are given a node that is the beginning of a linked list. This list always contains a tail and a loop. Your objective is to determine the length of the loop.

# For example in the following picture the tail's size is 3 and the loop size is 12:


# # Use the `next' attribute to get the following node
# node.next
# Note: do NOT mutate the nodes!

# Thanks to shadchnev, I broke all of the methods from the Hash class.

# Don't miss dmitry's article in the discussion after you pass the Kata !! 
# I couldn't figure this one out. 

def loop_size(node):
    size = 0
    onestep = node
    twostep = node.next
    while(onestep != twostep):
        twostep = twostep.next.next
        onestep = onestep.next
    #we are inside the loop
    #onestep == twostep
    onestep = onestep.next
    size += 1
    while(onestep != twostep):
        size += 1
        onestep = onestep.next
    return size