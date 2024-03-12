import subprocess

def execute_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout, stderr

def main():
    while True:
        command = input("$ ")
        if command.lower() == "exit":
            break
        stdout, stderr = execute_command(command)
        if stdout:
            print(stdout.decode())
        if stderr:
            print(stderr.decode())

if __name__ == "__main__":
    main()
