val = 0xCAFE


t = (val & 1) + ((val >> 1) & 1) + ((val >> 2) & 1) + ((val >> 3) & 1)
ok = t >= 3
print("3 of last 4 bits on:", ok)


rev = ((val >> 8) & 0xFF) | ((val & 0xFF) << 8)
print("reversed:", hex(rev))


rot = ((val << 4) | (val >> 12)) & 0xFFFF
print("rotated:", hex(rot))
