tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

# 1. Check whether the dictionary contains the key 'Canada'.
print('1:', 'Canada' in tlds)

# 2. Check whether the dictionary contains the key 'France'.
print('2:', 'France' in tlds)

# 3. Iterate through the key–value pairs and display them in a two-column format.
print('3:')
for country, domain in tlds.items():
    print(f'{country:<15} {domain}')

# 4. Add the key–value pair 'Sweden' and 'sw' (which is incorrect).
tlds['Sweden'] = 'sw'

# 5. Update the value for the key 'Sweden' to 'se'.
tlds['Sweden'] = 'se'
print('5:', tlds)

# 6. Use dictionary comprehension to reverse the keys and values.
reversed_tlds = {value: key for key, value in tlds.items()}
print('6:', reversed_tlds)

# 7. With the result of part (f), use a dictionary comprehension to convert the country names to all uppercase letters.
uppercase_tlds = {key: value.upper() for key, value in reversed_tlds.items()}
print('7:', uppercase_tlds)
