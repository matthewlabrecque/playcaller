import export_pkg_kickstart
import detect_pkg_manager
import ansible_runner

def main():
    pm = detect_pkg_manager()

    export_pkg_kickstart()

if __name__ == "__main__":
    main()