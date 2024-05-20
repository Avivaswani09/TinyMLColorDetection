import pyfirmata

comport='COM5'

board=pyfirmata.Arduino(comport)

led_r = board.get_pin('d:11:p')
led_g = board.get_pin('d:10:p')
led_b = board.get_pin('d:9:p')


def led(myColor):
  a=myColor[0]
  b=myColor[1]
  c=myColor[2]



  led_r_value = a / 255.0
  led_g_value = b / 255.0
  led_b_value = c / 755.0

  led_r.write(led_r_value)
  led_g.write(led_g_value)
  led_b.write(led_b_value)





# import pyfirmata

# comport = 'COM5'

# board = pyfirmata.Arduino(comport)

# led_r = board.get_pin('d:11:p')
# led_g = board.get_pin('d:10:p')
# led_b = board.get_pin('d:9:p')

# def led(myColor):
#     a = myColor[0]
#     b = myColor[1]
#     c = myColor[2]

#     max_color = max(a, b, c)

#     if max_color == a:
#         led_r_value = a / 255.0
#         led_g_value = 0.0
#         led_b_value = 0.0
#     elif max_color == b:
#         led_r_value = 0.0
#         led_g_value = b / 255.0
#         led_b_value = 0.0
#     else:
#         led_r_value = 0.0
#         led_g_value = 0.0
#         led_b_value = c / 255.0

#     led_r.write(led_r_value)
#     led_g.write(led_g_value)
#     led_b.write(led_b_value)

