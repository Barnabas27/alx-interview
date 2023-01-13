#!/usr/bin/python3
'''Min Operations python3 challenge'''


def minOperations(n):
    '''calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns:
        int  and if impossible > return 0
    '''
    pasted_chars = 1  # chars in the file
    clipboard = 0  # number of H's copied
    counter = 0  # 

    while pasted_chars < n:
        
        if clipboard == 0:
            
            clipboard = pasted_chars
            
            counter += 1

        
        if pasted_chars == 1:
            
            pasted_chars += clipboard
            
            counter += 1
            
            continue

        remaining = n - pasted_chars  # remaining chars to Paste
        
        if remaining < clipboard:
            return 0

        
        if remaining % pasted_chars != 0:
            
            pasted_chars += clipboard
           
            counter += 1
        else:
            
            clipboard = pasted_chars
            
            pasted_chars += clipboard
            
            counter += 2

    
    if pasted_chars == n:
        return counter
    else:
        return 0
        