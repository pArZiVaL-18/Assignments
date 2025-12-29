def snake_to_camal(s):
     s = s.split("_")
     ans = s[0]
     for i in range(1, len(s)):
          ans += s[i][0].upper() + s[i][1:]
     return ans

print(snake_to_camal("roshan_malkar_hi123"))
print(snake_to_camal("what_the_heck_is_this"))
