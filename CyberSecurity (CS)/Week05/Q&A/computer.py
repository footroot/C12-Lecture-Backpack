class Computer:
    def __init__(self, operating_system, cpu, gpu, ram, psu, storage):
        """Initialize the computer with its components."""
        self.operating_system = operating_system
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.psu = psu
        self.storage = storage

    def boot_up(self):
        """Simulate booting up the computer."""
        print(f"Booting up the computer with {self.operating_system}...")

    def shut_down(self):
        """Simulate shutting down the computer."""
        print("Shutting down the computer...")

    def install_software(self, software_name):
        """Simulate installing software on the computer."""
        print(f"Installing {software_name} on the computer...")

    def run_program(self, program_name):
        """Simulate running a program on the computer."""
        print(f"Running {program_name} on the computer...")

    def check_specs(self):
        """Print the specifications of the computer."""
        print("Computer Specifications:")
        print(f"Operating System: {self.operating_system}")
        print(f"CPU: {self.cpu}")
        print(f"GPU: {self.gpu}")
        print(f"RAM: {self.ram} GB")
        print(f"PSU: {self.psu} W")
        print(f"Storage: {self.storage} GB")

# Example usage
my_computer = Computer("Windows 11", "AMD Ryzen 9 5900X", "NVIDIA RTX 3080", 32, 750, 2000)

my_computer.boot_up()
my_computer.check_specs()
my_computer.install_software("Python 3.10")
my_computer.run_program("Visual Studio Code")
my_computer.shut_down()
