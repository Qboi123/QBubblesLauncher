import os

from compiler import Compiler

if __name__ == '__main__':
    # Get main folder
    main_folder_ = os.getcwd()

    # Compiler class
    compiler = Compiler(
        exclude=[".idea", ".gitattributes", ".gitignore", "build.py", "README.md",
                 "obj", "icon.png", ".git", "compiler.py", "dll", "game", "downloads", "out.png", "account.json",
                 "launcher_profiles.json", "args.txt"],
        icon=None, main_folder=os.getcwd(), main_file="main.py",
        hidden_imports=["os", "tkinter", "tkinter.tix", "_tkinter", "_tkinter.tix", "tkinter.filedialog", "_io",
                        "pmlauncher.mdownloader", "pmlauncher.mevent", "pmlauncher.minecraft", "pmlauncher.pycraft",
                        "pmlauncher.pycraft.authentication", "pmlauncher.mdownloader", "pmlauncher.mlaunch",
                        "pmlauncher.mlaunchoption", "pmlauncher.mlibrary", "pmlauncher.mlogin",
                        "pmlauncher.mprofile", "pmlauncher.mnative", "pmlauncher.mprofileinfo", "pmlauncher.mrule",
                        "pmlauncher.pml", "pmlauncher.pycraft.networking", "pmlauncher.pycraft.compat",
                        "pmlauncher.pycraft.exceptions"],
        log_level="INFO", app_name="QMinecraftLauncher", clean=True, hide_console=False, one_file=False, uac_admin=False)

    # TODO: Add needed pmlauncher modules
    compiler.reindex()

    # Get argument and command
    args = compiler.get_args()
    command = compiler.get_command(args)

    # Compile workspace
    compiler.compile(command)
