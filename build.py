import os

from compiler import Compiler

if __name__ == '__main__':
    # Get main folder
    main_folder_ = os.getcwd()

    # Compiler class
    compiler = Compiler(
        exclude=[".idea", ".gitattributes", ".gitignore", "build.py", "README.md",
                 "obj", "icon.png", ".git", "compiler.py", "dll", "game", "downloads", "out.png", "account.json",
                 "launcher_profiles.json", "args.txt", "src", "icons", "requirements.txt"],
        icon=None, main_folder=os.getcwd(), main_file="main.py",
        hidden_imports=["os", "tkinter", "tkinter.tix", "_tkinter", "_tkinter.tix", "tkinter.filedialog", "_io",
                        "pkg_resources.py2_warn"],
        log_level="INFO", app_name="QMinecraftLauncher", clean=True, hide_console=False, one_file=False, uac_admin=False)

    compiler.reindex()

    # Get argument and command
    args = compiler.get_args()
    command = compiler.get_command(args)

    # Compile workspace
    compiler.compile(command)
