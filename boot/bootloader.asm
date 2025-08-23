; Enhanced Bootloader for VMware and VirtualBox compatibility
; Minimal bootloader with GUI support

[ORG 0x7C00]        ; Boot sector loads at 0x7C00
[BITS 16]           ; 16-bit mode initially

start:
    ; Setup segments
    xor ax, ax      ; Clear AX
    mov ds, ax      ; Data segment = 0
    mov es, ax      ; Extra segment = 0
    mov ss, ax      ; Stack segment = 0
    mov sp, 0x7C00  ; Stack pointer just below boot sector

    ; Clear screen and set VGA text mode
    mov ah, 0x00    ; Set video mode
    mov al, 0x03    ; 80x25 text mode (compatible with VMware and VirtualBox)
    int 0x10        ; BIOS video interrupt

    ; Print welcome message
    mov si, welcome_msg
    call print_string

    ; Load kernel from disk (enhanced with error checking)
    mov ah, 0x02    ; Read sectors
    mov al, 4       ; Number of sectors to read (kernel is now 4 sectors for GUI)
    mov ch, 0       ; Cylinder 0
    mov cl, 2       ; Sector 2 (sector 1 is boot sector)
    mov dh, 0       ; Head 0
    mov dl, 0x80    ; Drive 0x80 (first hard drive)
    mov bx, 0x1000  ; Load kernel at 0x1000
    int 0x13        ; BIOS disk interrupt

    ; Check for read errors
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
    mov bl, 0x0F    ; White on black attribute (brighter)
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
welcome_msg     db 'Simple GUI OS - VMware & VirtualBox', 0x0D, 0x0A, 0
kernel_msg      db 'Starting GUI...', 0x0D, 0x0A, 0
error_msg       db 'Kernel load error!', 0x0D, 0x0A, 0

; Pad to 510 bytes and add boot signature
times 510-($-$$) db 0
dw 0xAA55           ; Boot signature for BIOS