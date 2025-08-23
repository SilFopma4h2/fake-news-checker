#!/bin/bash

# VMware VM Setup Script for Simple GUI OS
# This script helps create a VMware VM to run the Simple GUI OS

set -e

# Configuration
VM_NAME="Simple-GUI-OS"
OS_IMAGE="build/os.img"
VM_DIR="$HOME/vmware/$VM_NAME"
VMWARE_CMD="vmrun"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if VMware is installed
check_vmware() {
    if ! command -v vmrun &> /dev/null; then
        print_error "VMware Workstation/Player not found or vmrun not in PATH"
        print_error "Please install VMware Workstation or VMware Player"
        exit 1
    fi
    
    print_status "VMware found: $(vmrun | head -1)"
}

# Check if OS image exists
check_os_image() {
    if [ ! -f "$OS_IMAGE" ]; then
        print_error "OS image not found: $OS_IMAGE"
        print_error "Please build the OS first with: make"
        exit 1
    fi
    
    print_status "OS image found: $OS_IMAGE"
}

# Create VM directory
create_vm_dir() {
    if [ -d "$VM_DIR" ]; then
        print_warning "VM directory already exists: $VM_DIR"
        read -p "Do you want to remove it and create a new one? (y/N): " -r
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm -rf "$VM_DIR"
            print_status "Removed existing VM directory"
        else
            print_error "Aborted. Please remove the existing VM directory first."
            exit 1
        fi
    fi
    
    mkdir -p "$VM_DIR"
    print_status "Created VM directory: $VM_DIR"
}

# Create VMX configuration file
create_vmx() {
    print_status "Creating VMware configuration file..."
    
    cat > "$VM_DIR/$VM_NAME.vmx" << 'EOF'
#!/usr/bin/vmware
.encoding = "UTF-8"
config.version = "8"
virtualHW.version = "19"
pciBridge0.present = "TRUE"
pciBridge4.present = "TRUE"
pciBridge4.virtualDev = "pcieRootPort"
pciBridge4.functions = "8"
pciBridge5.present = "TRUE"
pciBridge5.virtualDev = "pcieRootPort"
pciBridge5.functions = "8"
pciBridge6.present = "TRUE"
pciBridge6.virtualDev = "pcieRootPort"
pciBridge6.functions = "8"
pciBridge7.present = "TRUE"
pciBridge7.virtualDev = "pcieRootPort"
pciBridge7.functions = "8"
vmci0.present = "TRUE"
displayName = "Simple GUI OS"
guestOS = "other"
numvcpus = "1"
memsize = "512"
firmware = "bios"
powerType.powerOff = "soft"
powerType.powerOn = "hard"
powerType.suspend = "hard"
powerType.reset = "soft"

# IDE Controller for the OS image
ide0:0.present = "TRUE"
ide0:0.fileName = "os.img"
ide0:0.deviceType = "rawDisk"

# Floppy drive disabled
floppy0.present = "FALSE"

# Network adapter
ethernet0.present = "TRUE"
ethernet0.virtualDev = "e1000"
ethernet0.connectionType = "nat"

# USB controller
usb.present = "TRUE"
ehci.present = "TRUE"
usb.vbluetooth.startConnected = "FALSE"

# Sound
sound.present = "FALSE"

# Display settings
svga.graphicsMemoryKB = "16384"
svga.autodetect = "TRUE"

# Mouse and keyboard
mouse.present = "TRUE"
mouse.vusb.enable = "FALSE"
keyboard.present = "TRUE"
keyboard.vusb.enable = "FALSE"

# Tools
tools.syncTime = "FALSE"
tools.upgrade.policy = "upgradeAtPowerCycle"

# Clean shutdown
cleanShutdown = "TRUE"
EOF
    
    print_success "VMX configuration created"
}

# Copy OS image
copy_os_image() {
    print_status "Copying OS image to VM directory..."
    cp "$OS_IMAGE" "$VM_DIR/os.img"
    print_success "OS image copied"
}

# Main setup function
main() {
    echo "========================================="
    echo "Simple GUI OS - VMware VM Setup"
    echo "========================================="
    echo
    
    print_status "Checking prerequisites..."
    check_vmware
    check_os_image
    
    print_status "Setting up VMware VM..."
    create_vm_dir
    create_vmx
    copy_os_image
    
    echo
    print_success "VMware VM created successfully!"
    echo
    echo "VM Details:"
    echo "  Name: $VM_NAME"
    echo "  Location: $VM_DIR"
    echo "  Memory: 512MB"
    echo "  CPU: 1 core"
    echo "  Firmware: BIOS"
    echo "  Storage: IDE with Simple GUI OS"
    echo
    echo "To start the VM:"
    echo "  vmrun start \"$VM_DIR/$VM_NAME.vmx\""
    echo "  or use VMware Workstation/Player GUI"
    echo
    echo "GUI OS Features:"
    echo "  - Boots to graphical desktop"
    echo "  - Mouse support with clickable elements"
    echo "  - System information window"
    echo "  - ESC key switches to text mode"
    echo "  - Text mode commands: h, i, g, r, s"
    echo
}

# Run main function
main "$@"