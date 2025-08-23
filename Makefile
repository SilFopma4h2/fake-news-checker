# Makefile for Simple OS - VirtualBox Compatible
# Builds a bootable OS image that can run in VirtualBox

# Tools
ASM = nasm
DD = dd
QEMU = qemu-system-i386

# Directories
BOOT_DIR = boot
KERNEL_DIR = kernel
BUILD_DIR = build

# Files
BOOTLOADER = $(BOOT_DIR)/bootloader.asm
KERNEL = $(KERNEL_DIR)/kernel.asm
BOOTLOADER_BIN = $(BUILD_DIR)/bootloader.bin
KERNEL_BIN = $(BUILD_DIR)/kernel.bin
OS_IMAGE = $(BUILD_DIR)/os.img
ISO_IMAGE = $(BUILD_DIR)/os.iso

# Default target
all: $(OS_IMAGE)

# Create build directory
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

# Build bootloader
$(BOOTLOADER_BIN): $(BOOTLOADER) | $(BUILD_DIR)
	$(ASM) -f bin $< -o $@

# Build kernel
$(KERNEL_BIN): $(KERNEL) | $(BUILD_DIR)
	$(ASM) -f bin $< -o $@

# Create OS image
$(OS_IMAGE): $(BOOTLOADER_BIN) $(KERNEL_BIN)
	# Create empty disk image (1440KB floppy size for VirtualBox compatibility)
	$(DD) if=/dev/zero of=$@ bs=1024 count=1440
	# Write bootloader to first sector
	$(DD) if=$(BOOTLOADER_BIN) of=$@ bs=512 count=1 conv=notrunc
	# Write kernel to second sector (2 sectors for kernel)
	$(DD) if=$(KERNEL_BIN) of=$@ bs=512 seek=1 count=2 conv=notrunc

# Create ISO image for VirtualBox
iso: $(ISO_IMAGE)

$(ISO_IMAGE): $(OS_IMAGE)
	# Create ISO directory structure
	mkdir -p $(BUILD_DIR)/iso
	cp $(OS_IMAGE) $(BUILD_DIR)/iso/
	# Create bootable ISO (requires mkisofs or genisoimage)
	if command -v mkisofs >/dev/null 2>&1; then \
		mkisofs -o $@ -b os.img -no-emul-boot -boot-load-size 4 -boot-info-table $(BUILD_DIR)/iso; \
	elif command -v genisoimage >/dev/null 2>&1; then \
		genisoimage -o $@ -b os.img -no-emul-boot -boot-load-size 4 -boot-info-table $(BUILD_DIR)/iso; \
	else \
		echo "Warning: mkisofs or genisoimage not found. ISO creation skipped."; \
		echo "You can still use the raw image $(OS_IMAGE) in VirtualBox."; \
	fi

# Test with QEMU (if available)
test: $(OS_IMAGE)
	@if command -v $(QEMU) >/dev/null 2>&1; then \
		echo "Testing OS with QEMU..."; \
		$(QEMU) -drive format=raw,file=$<; \
	else \
		echo "QEMU not found. Please test manually in VirtualBox."; \
		echo "Use the image: $<"; \
	fi

# VirtualBox specific targets
vbox-info:
	@echo "VirtualBox Setup Instructions:"
	@echo "1. Create new VM: Type=Other, Version=Other/Unknown"
	@echo "2. Memory: 512MB minimum"
	@echo "3. Hard disk: Create new VDI, 10GB"
	@echo "4. System -> Motherboard: Disable EFI"
	@echo "5. Storage: Attach $(OS_IMAGE) or $(ISO_IMAGE) to IDE controller"
	@echo "6. Start VM"

# Check dependencies
check-deps:
	@echo "Checking dependencies..."
	@command -v $(ASM) >/dev/null 2>&1 || (echo "Error: nasm not found. Install with: apt-get install nasm" && exit 1)
	@command -v $(DD) >/dev/null 2>&1 || (echo "Error: dd not found" && exit 1)
	@echo "Dependencies OK"

# Clean build files
clean:
	rm -rf $(BUILD_DIR)

# Show help
help:
	@echo "Simple OS Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  all        - Build OS image (default)"
	@echo "  iso        - Create bootable ISO"
	@echo "  test       - Test with QEMU (if available)"
	@echo "  clean      - Remove build files"
	@echo "  check-deps - Check required dependencies"
	@echo "  vbox-info  - Show VirtualBox setup instructions"
	@echo "  help       - Show this help"
	@echo ""
	@echo "Files created:"
	@echo "  $(OS_IMAGE) - Raw disk image for VirtualBox"
	@echo "  $(ISO_IMAGE) - ISO image for VirtualBox CD/DVD"

.PHONY: all iso test clean check-deps vbox-info help