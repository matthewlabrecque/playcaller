# Support for BASH, ZSH, VIM, NEOVIM, and automation scripts using GNU STOW

import os
from datetime import datetime
from pathlib import Path

def import_bash_conf():
    with open(os.path.join(Path.home(), ".bashrc")) as data:
        user_bash_conf = data.read()
    return user_bash_conf

def import_zsh_conf():
    with open(os.path.join(Path.home(), ".zshrc")) as data:
        user_zsh_conf = data.read()
    return user_zsh_conf

def import_nvim_conf():
    with open(os.path.join(Path.home(), ".config/nvim/init.lua")) as data:
        user_nvim_conf = data.read()
    return user_nvim_conf

def main(config_type: str = "bash"):
    """
    Main function that returns values from other functions based on parameters.
    
    Args:
        config_type: Type of configuration to import ("bash", "zsh", "nvim")
    
    Returns:
        String containing the imported configuration content
    """
    config_type = config_type.lower()
    
    if config_type == "bash":
        return import_bash_conf()
    elif config_type == "zsh":
        return import_zsh_conf()
    elif config_type == "nvim":
        return import_nvim_conf()
    else:
        raise ValueError(f"Unknown configuration type: {config_type}. Use 'bash', 'zsh', or 'nvim'")

if __name__ == "__main__":
    main()