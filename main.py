from classes.CLI import cli
from classes.CLI import cli_main_menu as MENU

CLI_MANAGER: cli.CLIManager = cli.CLIManager()

cli.CLI.manager = CLI_MANAGER

MENU_PRINCIPAL: MENU.CLIMainMenu = MENU.CLIMainMenu()

CLI_MANAGER.change_gui(MENU_PRINCIPAL)

while True:
    CLI_MANAGER.update()
