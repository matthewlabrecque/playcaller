def detect_pkg_manager():
    """Checks for which package manager is installed and returns it."""
    if shutil.which("apt-get"):
        return "apt"
    elif shutil.which("dnf"):
        return "dnf"
    elif shutil.which("pacman"):
        return "pacman"
    elif shutil.which("brew"):
        return "brew"
    else:
        return None

def main():
    return detect_pkg_manager

if __name__ == "__main__":
    main()