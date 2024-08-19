from nicegui import ui,ElementFilter

def update():
    ui.notify(editor.value)
    exec(editor.value)

editor = ui.codemirror('print("Edit me!")', language='Python').classes('h-32')

ui.button('Click me!', on_click=update)

ui.run()
