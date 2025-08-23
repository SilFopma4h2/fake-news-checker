# Simple OS - VirtualBox Compatible

A minimal operating system designed to run in VirtualBox on Linux systems. This project serves as an educational example of OS development and virtualization.

## Quick Start

### Prerequisites
- `nasm` (Netwide Assembler)
- `make`
- VirtualBox installed on Linux

### Building
```bash
# Check dependencies
make check-deps

# Build the OS
make

# Create ISO for VirtualBox (optional)
make iso
```

### Running in VirtualBox

1. **Build the OS first**: `make`

2. **Create a new VM in VirtualBox**:
   - Name: Simple OS
   - Type: Other
   - Version: Other/Unknown (64-bit)
   - Memory: 512MB

3. **Configure VM settings**:
   - System → Motherboard: **Disable EFI** (important!)
   - System → Processor: 1 CPU
   - Storage: Create new hard disk (VDI, 10GB)

4. **Attach the OS image**:
   - Go to VM Settings → Storage
   - Add the `build/os.img` file as a hard disk, OR
   - Add the `build/os.iso` file to the optical drive

5. **Start the VM** - the OS should boot and display a simple command interface

### Available Commands in OS
- `h` - Show help
- `i` - Display system information  
- `r` - Reboot system
- `s` - Shutdown system

## Project Structure
```
.
├── boot/
│   └── bootloader.asm      # BIOS bootloader
├── kernel/
│   └── kernel.asm          # Simple kernel
├── build/                  # Generated files
│   ├── os.img             # Raw disk image
│   └── os.iso             # Bootable ISO
├── Makefile               # Build system
├── README.md              # This file
└── os_overview_mvp.md     # Detailed documentation
```

## Testing
```bash
# Test with QEMU (if available)
make test

# Get VirtualBox setup instructions
make vbox-info
```

## VirtualBox Compatibility Features

- **BIOS Boot**: Traditional BIOS booting (not UEFI)
- **Real Mode**: 16-bit x86 compatible with all VirtualBox versions
- **Standard VGA**: Text mode display that works reliably
- **PS/2 Input**: Keyboard input using standard PS/2 controller
- **ACPI Shutdown**: Graceful shutdown in VirtualBox environment

## Troubleshooting

### VM won't boot
- Ensure EFI is **disabled** in VM settings
- Check that the image file is properly attached
- Verify VM is set to "Other/Unknown" type

### Build issues
- Install nasm: `sudo apt-get install nasm`
- Install make: `sudo apt-get install make`
- Check file permissions in build directory

## Educational Notes

This OS demonstrates:
- Basic bootloader development
- Simple kernel implementation  
- VirtualBox virtualization compatibility
- Real mode x86 programming
- BIOS system calls

For detailed technical information, see `os_overview_mvp.md`.

## License

MIT License - See LICENSE file for details.