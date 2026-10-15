import sys
import platform


def main():
    print("=" * 50)
    print("Generative AI Development Environment")
    print("=" * 50)

    print(f"Python Version : {sys.version}")
    print(f"Platform       : {platform.system()} {platform.release()}")
    print(f"Architecture   : {platform.machine()}")

    print("\nEnvironment setup completed successfully.")
    print("Your system is ready for Generative AI development.")


if __name__ == "__main__":
    main()

