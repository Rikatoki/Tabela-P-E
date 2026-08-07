import classes.GUI.gui as gui
import classes.GUI.menu_principal as MENU

GUI_MANAGER: gui.GUIManager = gui.GUIManager()

gui.GUI.manager = GUI_MANAGER

MENU_PRINCIPAL: MENU.MenuPrincipal = MENU.MenuPrincipal()

GUI_MANAGER.change_gui(MENU_PRINCIPAL)

while True:
    GUI_MANAGER.update()
