# Simple GUI OS - VMware & VirtualBox Compatible

A lightweight GUI operating system designed to run in VMware and VirtualBox environments. This project demonstrates OS development with a graphical user interface and serves as an educational example of virtualization compatibility.

## ✨ Features

- **🖥️ GUI Desktop**: Graphical interface with mouse support
- **🎯 Dual Mode**: Switch between GUI and text mode (ESC key)
- **🖱️ Mouse Support**: PS/2 mouse with clickable interface elements
- **💻 VMware & VirtualBox**: Compatible with both virtualization platforms
- **⚡ Lightweight**: Minimal footprint (~2KB kernel)
- **🎮 Interactive**: System information windows, start button, desktop icons

## 🚀 Quick Start

### Prerequisites
- `nasm` (Netwide Assembler)
- `make`
- VMware Workstation/Player or VirtualBox

### Building
```bash
# Check dependencies
make check-deps

# Build the GUI OS
make

# Create ISO for optical drive (optional)
make iso
```

### Running in VMware

1. **Automated Setup (Recommended)**:
   ```bash
   # Build the OS first
   make
   
   # Run VMware setup script
   ./setup-vmware.sh
   ```

2. **Manual Setup**:
   - Create new VM in VMware Workstation/Player
   - Name: Simple GUI OS  
   - Type: Other
   - Version: Other (32-bit)
   - Memory: 512MB
   - Hard disk: Use existing disk → select `build/os.img`
   - Firmware: BIOS (not UEFI)

3. **Start the VM** - it will boot to the GUI desktop automatically

### Running in VirtualBox

1. **Create a new VM**:
   - Name: Simple GUI OS
   - Type: Other
   - Version: Other/Unknown (32-bit)  
   - Memory: 512MB

2. **Configure VM settings**:
   - System → Motherboard: **Disable EFI** (use BIOS)
   - System → Processor: 1 CPU
   - Storage: Create new hard disk (VDI, 10GB) OR attach `build/os.img`

3. **Start the VM** - boots to GUI desktop

### 🎮 Using the GUI OS

**GUI Mode** (default):
- **Desktop**: Blue background with system information window
- **Mouse**: Click and drag support
- **Start Button**: Green button in bottom-left
- **System Info**: Window with OS details and close button (X)
- **ESC Key**: Switch to text mode

**Text Mode** (press ESC in GUI):
- `h` - Show help and available commands
- `i` - Display detailed system information  
- `g` - Return to GUI mode
- `r` - Reboot the system
- `s` - Shutdown the system

## 📁 Project Structure
```
.
├── boot/
│   └── bootloader.asm      # Enhanced BIOS bootloader
├── kernel/
│   └── kernel.asm          # GUI kernel with graphics support
├── build/                  # Generated files
│   ├── os.img             # Raw disk image (VMware/VirtualBox)
│   └── os.iso             # Bootable ISO (optional)
├── Makefile               # Build system
├── setup-vmware.sh        # VMware VM setup script  
├── setup-vbox.sh          # VirtualBox VM setup script
├── README.md              # This file
└── os_overview_mvp.md     # Detailed documentation
```

## 🧪 Testing
```bash
# Test with QEMU (if available)
make test

# Get VMware/VirtualBox setup info
make help
make vbox-info
```

## 🎨 GUI Features

- **🖥️ VGA Graphics**: 320x200x256 color mode
- **🖱️ PS/2 Mouse**: Full mouse support with cursor
- **🪟 Windows**: Draggable system information window  
- **🎨 Desktop Elements**: Icons, start button, title bar
- **⌨️ Keyboard**: Switch modes and system control
- **💾 VMware Optimized**: Enhanced for VMware compatibility

## 🔧 Technical Details

- **Architecture**: x86 16-bit real mode
- **Graphics**: VGA Mode 13h (320x200x256)
- **Input**: PS/2 keyboard and mouse support
- **Boot**: BIOS bootloader (512 bytes) + GUI kernel (2048 bytes)
- **Memory**: Minimal RAM usage (<64KB)
- **Storage**: 1.44MB floppy image format

## 🚨 Troubleshooting

### VMware Issues
- **VM won't boot**: Ensure BIOS firmware is selected (not UEFI)
- **No mouse cursor**: Check that mouse is enabled in VM settings
- **Graphics problems**: Verify VM has sufficient video memory (16MB+)
- **File not found**: Make sure `build/os.img` exists - run `make` first

### VirtualBox Issues
- **Boot failure**: Disable EFI in VM settings → System → Motherboard
- **Black screen**: Try increasing video memory in Display settings
- **No keyboard/mouse**: Enable I/O APIC in System settings
- **ISO not working**: Use the raw `build/os.img` file instead

### General Issues
- **Build fails**: Install `nasm` with your package manager
- **Keyboard not working**: Try different VM keyboard settings
- **Can't switch modes**: ESC key switches from GUI to text mode

## 🎓 Enhanced Educational Features

This GUI OS demonstrates:
- **Bootloader Development**: Enhanced 16-bit assembly bootloader
- **Graphics Programming**: VGA mode setup and pixel manipulation  
- **Mouse Driver**: PS/2 mouse interrupt handling and cursor support
- **GUI Framework**: Basic window system with event handling
- **Virtualization**: Cross-platform compatibility (VMware + VirtualBox)
- **Memory Management**: Efficient real-mode memory usage
- **User Interface**: Desktop metaphor with clickable elements

## 🤝 Contributing

Contributions welcome! Focus areas:
- Enhanced GUI elements (menus, file manager)
- Better graphics primitives and fonts
- Sound support and multimedia
- Simple file system implementation
- Network stack basics
- 32-bit protected mode transition

## License

MIT License - See LICENSE file for details.