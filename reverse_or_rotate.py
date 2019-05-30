def revrot(strng, sz):
    if sz <= 0 or not strng or sz > len(strng):
        return ""
    else:
        chunks = [strng[i:i+sz] for i in range(0, len(strng), sz)]
        modified_strng = ""
        for chunk in chunks:
            if len(chunk) == sz:
                sum_of_digit_cubes = 0
                for digit in list(chunk):
                    sum_of_digit_cubes += int(digit)**3
                if sum_of_digit_cubes % 2 == 0:
                    modified_strng += chunk[::-1]
                else:
                    modified_strng += chunk[1:]+chunk[0]
        return modified_strng

revrot("733049910872815764", 5)