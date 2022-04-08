    return color(h, s, v)

 def get_color_values():

     proc_color = get_agent_location_color()

     h = round(hue(proc_color),2)
     s = round(saturation(proc_color),2)
     v = round(brightness(proc_color),2)

     return h,s,v

 def get_white():
