import PySimpleGUI as psg
viget = [
    [psg.Input(key = 'name', default_text='noname')],
    [psg.OptionMenu(values = [15,20,30,40], key = 'puter', default_value = 20 ), psg.Text("введите кол-во врагов")],
    [ psg.Input(key = 'chosec', disabled = True, default_text = '#000000' ), psg.ColorChooserButton('выбор цвета шара', key  = 'color')],
    [psg.Button("start", key = "baton")] 
]

window = psg.Window("okno", viget)
while 10000000>0:
    read = window.read()
    ivent = read[0]
    slovar = read[-1]
    if ivent == None:
        break
    if ivent == 'baton':
        print(slovar)
        break
