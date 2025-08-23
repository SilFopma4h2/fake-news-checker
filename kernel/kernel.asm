; Simple Kernel for VirtualBox
; This kernel provides basic functionality compatible with VirtualBox

[ORG 0x1000]        ; Kernel loads at 0x1000
[BITS 16]           ; Start in 16-bit mode

kernel_start:
    ; Setup segments for kernel
    mov ax, 0x1000
    mov ds, ax
    mov es, ax

    ; Clear screen again
    mov ah, 0x00
    mov al, 0x03
    int 0x10

    ; Print kernel startup message
    mov si, kernel_banner
    call print_string

    ; Print system information
    mov si, sys_info
    call print_string

    ; Print VirtualBox specific information
    mov si, vbox_info
    call print_string

    ; Print available commands
    mov si, commands_info
    call print_string

    ; Enter command loop
    jmp command_loop

command_loop:
    ; Print prompt
    mov si, prompt
    call print_string

    ; Read command (simplified)
    call read_char
    
    ; Check commands
    cmp al, 'h'
    je show_help
    cmp al, 'i'
    je show_info
    cmp al, 'r'
    je reboot
    cmp al, 's'
    je shutdown
    cmp al, 0x0D    ; Enter key
    je command_loop

    ; Unknown command
    mov si, unknown_cmd
    call print_string
    jmp command_loop

show_help:
    call newline
    mov si, help_text
    call print_string
    jmp command_loop

show_info:
    call newline
    mov si, info_text
    call print_string
    jmp command_loop

reboot:
    call newline
    mov si, reboot_msg
    call print_string
    ; Reboot using keyboard controller
    mov al, 0xFE
    out 0x64, al
    hlt

shutdown:
    call newline
    mov si, shutdown_msg
    call print_string
    ; Attempt VirtualBox ACPI shutdown
    mov ax, 0x2000
    mov dx, 0x604
    out dx, ax
    hlt

; Print character in AL
print_char:
    push ax
    push bx
    mov ah, 0x0E
    mov bh, 0
    mov bl, 0x07
    int 0x10
    pop bx
    pop ax
    ret

; Print string pointed to by SI
print_string:
    push ax
    push bx
    mov ah, 0x0E
    mov bh, 0
    mov bl, 0x07
.loop:
    lodsb
    test al, al
    jz .done
    int 0x10
    jmp .loop
.done:
    pop bx
    pop ax
    ret

; Read single character
read_char:
    mov ah, 0x00
    int 0x16        ; BIOS keyboard interrupt
    ; Echo character
    call print_char
    ret

; Print newline
newline:
    push ax
    mov al, 0x0D
    call print_char
    mov al, 0x0A
    call print_char
    pop ax
    ret

; Messages and data
kernel_banner   db '==========================================', 0x0D, 0x0A
                db '    Simple OS Kernel - VirtualBox Ready   ', 0x0D, 0x0A
                db '==========================================', 0x0D, 0x0A, 0

sys_info        db 'System Information:', 0x0D, 0x0A
                db '- Architecture: x86 (16-bit)', 0x0D, 0x0A
                db '- Memory: Real mode addressing', 0x0D, 0x0A
                db '- Display: VGA Text Mode', 0x0D, 0x0A, 0

vbox_info       db 'VirtualBox Compatibility:', 0x0D, 0x0A
                db '- BIOS boot supported', 0x0D, 0x0A
                db '- Standard VGA display', 0x0D, 0x0A
                db '- PS/2 keyboard input', 0x0D, 0x0A
                db '- ACPI shutdown available', 0x0D, 0x0A, 0

commands_info   db 'Available Commands:', 0x0D, 0x0A
                db '- h: Show help', 0x0D, 0x0A
                db '- i: System information', 0x0D, 0x0A
                db '- r: Reboot system', 0x0D, 0x0A
                db '- s: Shutdown system', 0x0D, 0x0A, 0x0D, 0x0A, 0

prompt          db 'OS> ', 0

help_text       db 'Simple OS Help:', 0x0D, 0x0A
                db 'This is a minimal operating system designed for VirtualBox.', 0x0D, 0x0A
                db 'Type a command letter and press Enter.', 0x0D, 0x0A, 0

info_text       db 'System Status: Running in VirtualBox', 0x0D, 0x0A
                db 'Kernel loaded at 0x1000', 0x0D, 0x0A
                db 'Text mode: 80x25 VGA', 0x0D, 0x0A, 0

unknown_cmd     db ' - Unknown command (try h for help)', 0x0D, 0x0A, 0

reboot_msg      db 'Rebooting system...', 0x0D, 0x0A, 0
shutdown_msg    db 'Shutting down...', 0x0D, 0x0A, 0

; Pad kernel to multiple sectors if needed
times 1024-($-$$) db 0