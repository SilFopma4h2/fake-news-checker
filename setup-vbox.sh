#!/bin/bash
# VirtualBox setup script for Simple OS
# This script helps configure VirtualBox for the Simple OS

set -e

# Configuration
VM_NAME="Simple-OS"
OS_IMAGE="build/os.img"
VBOX_MANAGE="VBoxManage"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if VirtualBox is installed
if ! command -v $VBOX_MANAGE &> /dev/null; then
    print_error "VirtualBox is not installed or VBoxManage is not in PATH"
    print_error "Please install VirtualBox first"
    exit 1
fi

# Check if OS image exists
if [ ! -f "$OS_IMAGE" ]; then
    print_error "OS image not found: $OS_IMAGE"
    print_error "Please build the OS first with: make"
    exit 1
fi

# Check if VM already exists
if $VBOX_MANAGE list vms | grep -q "$VM_NAME"; then
    print_warning "VM '$VM_NAME' already exists"
    read -p "Do you want to delete it and create a new one? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        print_status "Removing existing VM..."
        $VBOX_MANAGE unregistervm "$VM_NAME" --delete 2>/dev/null || true
    else
        print_error "Aborted. Please remove the existing VM first or use a different name."
        exit 1
    fi
fi

print_status "Creating VirtualBox VM for Simple OS..."

# Create VM
print_status "Creating VM '$VM_NAME'..."
$VBOX_MANAGE createvm --name "$VM_NAME" --ostype "Other" --register

# Configure VM settings
print_status "Configuring VM settings..."
$VBOX_MANAGE modifyvm "$VM_NAME" \
    --memory 512 \
    --cpus 1 \
    --firmware bios \
    --boot1 disk \
    --boot2 none \
    --boot3 none \
    --boot4 none \
    --acpi on \
    --ioapic off \
    --rtcuseutc on \
    --hwvirtex on \
    --nestedpaging on \
    --largepages off \
    --vtxvpid on \
    --accelerate3d off \
    --accelerate2dvideo off

# Create storage controller
print_status "Creating storage controller..."
$VBOX_MANAGE storagectl "$VM_NAME" \
    --name "IDE Controller" \
    --add ide \
    --controller PIIX4

# Convert and attach OS image
print_status "Converting OS image to VDI format..."
CONVERTED_IMAGE="build/os.vdi"
$VBOX_MANAGE convertfromraw "$OS_IMAGE" "$CONVERTED_IMAGE" --format VDI

print_status "Attaching OS image to VM..."
$VBOX_MANAGE storageattach "$VM_NAME" \
    --storagectl "IDE Controller" \
    --port 0 \
    --device 0 \
    --type hdd \
    --medium "$CONVERTED_IMAGE"

# Configure display
print_status "Configuring display..."
$VBOX_MANAGE modifyvm "$VM_NAME" \
    --graphicscontroller vga \
    --vram 16 \
    --monitorcount 1

print_status "VM '$VM_NAME' created successfully!"
print_status ""
print_status "To start the VM:"
print_status "  VBoxManage startvm '$VM_NAME'"
print_status "  or use the VirtualBox GUI"
print_status ""
print_status "VM Configuration:"
print_status "  - Memory: 512MB"
print_status "  - CPUs: 1"
print_status "  - Firmware: BIOS (not UEFI)"
print_status "  - Storage: IDE controller with OS image"
print_status ""
print_status "The OS should boot automatically and display a command prompt."
print_status "Available commands in the OS: h, i, r, s"