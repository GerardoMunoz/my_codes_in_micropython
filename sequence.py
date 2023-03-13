from machine import Pin,Timer
pin_led = Pin(25, mode=Pin.OUT)
pin_button = Pin(0, mode=Pin.IN, pull=Pin.PULL_UP)

ctx={
        #"actual_state":"start",
        "seq_values":[1,0,1,0,1,0,1,1],
        "seq_index":0,
    }

def seq(t:Timer):
    global ctx
    button_in=pin_button()
    index=ctx["seq_index"]
    values=ctx["seq_values"]
    ######################
    value = values[index]
    pin_led(value)
    if value  == button_in:
        msg="bien"
    else:
        msg="mal"
    print(index,msg,value  , button_in)
    #######################
    index += 1
    if index >= len(values):
        index = 0
    ctx["seq_index"] = index
    



print("Siga la secuencia:", ctx["seq_values"])

Timer().init(mode=Timer.PERIODIC, period= 1000, callback=seq)

