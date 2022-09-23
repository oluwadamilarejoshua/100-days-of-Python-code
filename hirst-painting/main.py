import colorgram

color_list = colorgram.extract('hirst.jpg', 54)
# print(color_list[0].rgb)

the_list = []

for count in color_list:
    r = count.rgb.r
    g = count.rgb.g
    b = count.rgb.b
    ind_color = (r, g, b)
    the_list.append(ind_color)

print(the_list)
