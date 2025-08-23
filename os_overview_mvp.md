# OS Overview - MVP

This is a minimal viable product (MVP) of a simple operating system designed to run on VirtualBox with Linux kernel compatibility.

## Features

- **Bootable OS**: Simple bootloader that can start the system
- **VirtualBox Compatible**: Designed to run in VirtualBox virtualization environment
- **Linux Kernel Integration**: Compatible with Linux kernel infrastructure
- **Minimal Footprint**: Lightweight design suitable for learning and development

## Architecture

The OS consists of:
- **Boot Sector**: Initial bootloader code that starts the system
- **Kernel**: Basic kernel with essential system calls
- **Build System**: Makefile for easy compilation and image creation

## Building the OS

To build the OS, you'll need:
- `nasm` (Netwide Assembler)
- `gcc` (GNU Compiler Collection) 
- `make`
- `qemu` (for testing, optional)

```bash
# Build the OS image
make

# Create bootable ISO (optional)
make iso
```

## Running in VirtualBox

1. **Create a new VM in VirtualBox**:
   - Type: Other
   - Version: Other/Unknown
   - Memory: 512MB (minimum)
   - Hard disk: Create new, VDI, 10GB

2. **Configure the VM**:
   - System → Motherboard: Disable EFI
   - System → Processor: 1 CPU is sufficient
   - Storage: Attach the generated ISO file to the optical drive

3. **Boot the OS**:
   - Start the VM
   - The OS should boot directly from the ISO

## VirtualBox Compatibility Features

- **BIOS Boot**: Uses traditional BIOS booting for maximum compatibility
- **VGA Text Mode**: Simple text output that works with VirtualBox's display emulation
- **PS/2 Keyboard**: Basic keyboard input using PS/2 controller
- **Standard Hardware**: Avoids advanced hardware features for better virtualization support

## Development Notes

This OS is designed as a learning project and demonstrates:
- Basic bootloader development
- Simple kernel initialization
- VirtualBox virtualization compatibility
- Minimal system requirements

## File Structure

```
.
├── boot/           # Bootloader code
├── kernel/         # Kernel source
├── Makefile        # Build system
├── os_overview_mvp.md  # This documentation
└── README.md       # Basic project information
```

## Troubleshooting

### VirtualBox Boot Issues
- Ensure EFI is disabled in VM settings
- Verify the ISO file is properly attached
- Check that virtualization is enabled in BIOS/UEFI

### Build Issues
- Install required development tools
- Check that `nasm` and `gcc` are in PATH
- Ensure proper permissions on build files

## Contributing

This is an educational project. Contributions should focus on:
- Improving VirtualBox compatibility
- Adding basic system features
- Enhancing documentation
- Bug fixes and stability improvements

## License

MIT License - see LICENSE file for details.