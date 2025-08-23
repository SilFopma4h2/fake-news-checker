; Simple Bootloader for VirtualBox compatibility
; This bootloader is designed to work well in VirtualBox environment

[ORG 0x7C00]        ; Boot sector loads at 0x7C00
[BITS 16]           ; 16-bit mode initially

start:
    ; Setup segments
    xor ax, ax      ; Clear AX
    mov ds, ax      ; Data segment = 0
    mov es, ax      ; Extra segment = 0
    mov ss, ax      ; Stack segment = 0
    mov sp, 0x7C00  ; Stack pointer just below boot sector

    ; Clear screen (VirtualBox compatible)
    mov ah, 0x00    ; Set video mode
    mov al, 0x03    ; 80x25 text mode (VirtualBox default)
    int 0x10        ; BIOS video interrupt

    ; Print welcome message
    mov si, welcome_msg
    call print_string

    ; Print VirtualBox compatibility info
    mov si, vbox_msg
    call print_string

    ; Load kernel from disk (simplified for VirtualBox)
    mov ah, 0x02    ; Read sectors
    mov al, 2       ; Number of sectors to read (kernel is 2 sectors)
    mov ch, 0       ; Cylinder 0
    mov cl, 2       ; Sector 2 (sector 1 is boot sector)
    mov dh, 0       ; Head 0
    mov dl, 0x80    ; Drive 0x80 (first hard drive)
    mov bx, 0x1000  ; Load kernel at 0x1000
    int 0x13        ; BIOS disk interrupt

    ; Jump to kernel if load was successful
    jnc jump_to_kernel

    ; Display error if kernel load failed
    mov si, error_msg
    call print_string
    jmp hang

jump_to_kernel:
    mov si, kernel_msg
    call print_string
    jmp 0x1000      ; Jump to loaded kernel

hang:
    hlt             ; Halt processor
    jmp hang        ; Infinite loop

; Print string function (SI points to string)
print_string:
    push ax
    push bx
    mov ah, 0x0E    ; BIOS teletype output
    mov bh, 0       ; Page number 0
    mov bl, 0x07    ; White on black attribute
.next_char:
    lodsb           ; Load byte from SI into AL
    test al, al     ; Check if null terminator
    jz .done
    int 0x10        ; Print character
    jmp .next_char
.done:
    pop bx
    pop ax
    ret

; Messages
welcome_msg db 'Simple OS - VirtualBox Compatible', 0x0D, 0x0A, 0
vbox_msg    db 'Designed for VirtualBox on Linux', 0x0D, 0x0A, 0
kernel_msg  db 'Loading kernel...', 0x0D, 0x0A, 0
error_msg   db 'Error: Could not load kernel!', 0x0D, 0x0A, 0

; Pad to 510 bytes and add boot signature
times 510-($-$$) db 0
dw 0xAA55           ; Boot signature for BIOS