friends = ['Kishan', 'yash', 'ayush', 'yogesh']
print(f"friends id: {id(friends)}")
print(f"friends : {friends}")

# appendin new friend(item in list)
friends.append('aman')
print(f"friends id: {id(friends)}")
print(f"friends : {friends}")

# removing the friend 
friends.remove('Kishan')
print(f"friends : {friends}")

# Friends from diffrent sections
friends_diff_sections = ['amit', 'piyush']
friends.extend(friends_diff_sections);
print(f"friends : {friends}")

# remove the last enterd friend
print(f"popped friend: {friends.pop()}")

# Operator oveloading
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mic: {full_liquid_mix}")

strong_mix = ["masala", "chat-masala"] * 3;
print(f"strong mix: {strong_mix}")

salutations = bytearray(b"Good Morning!")
new_salutations = salutations.replace(b"Morning", b"Night");
print(f"new salutations: {new_salutations}")

