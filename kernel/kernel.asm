; Enhanced Kernel with GUI support for VMware and VirtualBox
; This kernel provides GUI functionality compatible with both VMware and VirtualBox

[ORG 0x1000]        ; Kernel loads at 0x1000
[BITS 16]           ; Start in 16-bit mode

kernel_start:
    ; Setup segments for kernel
    mov ax, 0x1000
    mov ds, ax
    mov es, ax

    ; Initialize GUI system
    call init_gui

    ; Display startup screen
    call display_startup
    
    ; Initialize mouse driver
    call init_mouse

    ; Enter main GUI loop
    jmp gui_main_loop

; Initialize GUI system
init_gui:
    ; Set VGA graphics mode 320x200x256 (Mode 13h)
    mov ah, 0x00
    mov al, 0x13    ; VGA 256-color mode
    int 0x10        ; Set video mode

    ; Clear screen with blue background
    call clear_screen_blue
    
    ; Draw desktop background
    call draw_desktop
    ret

; Clear screen with blue background (color 1 = blue)
clear_screen_blue:
    push ax
    push cx
    push di
    
    mov ax, 0xA000  ; VGA video memory segment
    mov es, ax
    xor di, di      ; Start at beginning of video memory
    mov ax, 0x0101  ; Blue color (1) in both bytes
    mov cx, 32000   ; 320x200 / 2 (since we're writing words)
    rep stosw       ; Fill video memory
    
    pop di
    pop cx
    pop ax
    ret

; Draw desktop background and basic GUI elements
draw_desktop:
    ; Draw title bar at top
    call draw_title_bar
    
    ; Draw desktop icon
    call draw_desktop_icon
    
    ; Draw start button
    call draw_start_button
    
    ; Draw system info window
    call draw_info_window
    ret

; Draw title bar
draw_title_bar:
    push ax
    push bx
    push cx
    push dx
    
    ; Draw a gray title bar (color 8 = dark gray)
    mov ax, 0xA000
    mov es, ax
    mov di, 0       ; Start at top of screen
    mov ax, 0x0808  ; Dark gray color
    mov cx, 6400    ; 320 pixels * 20 lines / 2 (words)
    rep stosw
    
    ; Draw title text "Simple OS GUI"
    mov ax, 10      ; X position
    mov bx, 5       ; Y position
    mov si, title_text
    mov dl, 15      ; White color
    call draw_text
    
    pop dx
    pop cx
    pop bx
    pop ax
    ret

; Draw desktop icon (system folder)
draw_desktop_icon:
    push ax
    push bx
    push cx
    push dx
    
    ; Draw icon background (light gray box)
    mov ax, 30      ; X position
    mov bx, 40      ; Y position
    mov cx, 32      ; Width
    mov dx, 32      ; Height
    mov dl, 7       ; Light gray color
    call draw_filled_rect
    
    ; Draw icon border (black)
    mov ax, 30      ; X position
    mov bx, 40      ; Y position
    mov cx, 32      ; Width
    mov dx, 32      ; Height
    mov dl, 0       ; Black color
    call draw_rect
    
    ; Draw icon label
    mov ax, 25      ; X position
    mov bx, 75      ; Y position
    mov si, icon_text
    mov dl, 15      ; White color
    call draw_text
    
    pop dx
    pop cx
    pop bx
    pop ax
    ret

; Draw start button
draw_start_button:
    push ax
    push bx
    push cx
    push dx
    
    ; Draw button background (green)
    mov ax, 10      ; X position
    mov bx, 180     ; Y position (near bottom)
    mov cx, 60      ; Width
    mov dx, 15      ; Height
    mov dl, 2       ; Green color
    call draw_filled_rect
    
    ; Draw button border (black)
    mov ax, 10      ; X position
    mov bx, 180     ; Y position
    mov cx, 60      ; Width
    mov dx, 15      ; Height
    mov dl, 0       ; Black color
    call draw_rect
    
    ; Draw button text
    mov ax, 20      ; X position
    mov bx, 185     ; Y position
    mov si, start_text
    mov dl, 15      ; White color
    call draw_text
    
    pop dx
    pop cx
    pop bx
    pop ax
    ret

; Draw system information window
draw_info_window:
    push ax
    push bx
    push cx
    push dx
    
    ; Draw window background (light blue)
    mov ax, 100     ; X position
    mov bx, 50      ; Y position
    mov cx, 200     ; Width
    mov dx, 120     ; Height
    mov dl, 3       ; Light blue color
    call draw_filled_rect
    
    ; Draw window border (black)
    mov ax, 100     ; X position
    mov bx, 50      ; Y position
    mov cx, 200     ; Width
    mov dx, 120     ; Height
    mov dl, 0       ; Black color
    call draw_rect
    
    ; Draw window title bar (dark blue)
    mov ax, 100     ; X position
    mov bx, 50      ; Y position
    mov cx, 200     ; Width
    mov dx, 15      ; Height
    mov dl, 1       ; Dark blue color
    call draw_filled_rect
    
    ; Draw window title
    mov ax, 110     ; X position
    mov bx, 55      ; Y position
    mov si, window_title
    mov dl, 15      ; White color
    call draw_text
    
    ; Draw window content
    mov ax, 110     ; X position
    mov bx, 75      ; Y position
    mov si, sys_info1
    mov dl, 0       ; Black color
    call draw_text
    
    mov ax, 110     ; X position
    mov bx, 90      ; Y position
    mov si, sys_info2
    mov dl, 0       ; Black color
    call draw_text
    
    mov ax, 110     ; X position
    mov bx, 105     ; Y position
    mov si, sys_info3
    mov dl, 0       ; Black color
    call draw_text
    
    mov ax, 110     ; X position
    mov bx, 120     ; Y position
    mov si, sys_info4
    mov dl, 0       ; Black color
    call draw_text
    
    mov ax, 110     ; X position
    mov bx, 135     ; Y position
    mov si, sys_info5
    mov dl, 0       ; Black color
    call draw_text
    
    ; Draw close button (X)
    mov ax, 280     ; X position (top right)
    mov bx, 50      ; Y position
    mov cx, 15      ; Width
    mov dx, 15      ; Height
    mov dl, 4       ; Red color
    call draw_filled_rect
    
    mov ax, 285     ; X position
    mov bx, 55      ; Y position
    mov si, close_x
    mov dl, 15      ; White color
    call draw_text
    
    pop dx
    pop cx
    pop bx
    pop ax
    ret

; Main GUI event loop
gui_main_loop:
    ; Check for mouse input
    call check_mouse
    
    ; Check for keyboard input
    mov ah, 0x01    ; Check if key available
    int 0x16
    jz gui_main_loop ; No key pressed, continue loop
    
    ; Read the key
    mov ah, 0x00
    int 0x16        ; Get keystroke
    
    ; Handle key presses
    cmp al, 0x1B    ; ESC key
    je text_mode    ; Switch to text mode
    cmp al, 'r'     ; R key
    je reboot
    cmp al, 's'     ; S key  
    je shutdown
    cmp al, 'g'     ; G key - return to graphics
    je init_gui
    
    jmp gui_main_loop ; Continue GUI loop

; Switch to text mode for command interface
text_mode:
    ; Set text mode
    mov ah, 0x00
    mov al, 0x03    ; 80x25 text mode
    int 0x10
    
    ; Clear screen and show text interface
    mov si, text_mode_msg
    call print_string_text
    
    ; Enter text command loop
    jmp text_command_loop

text_command_loop:
    ; Print prompt
    mov si, prompt
    call print_string_text

    ; Read command
    call read_char_text
    
    ; Check commands
    cmp al, 'h'
    je show_help
    cmp al, 'i'
    je show_info
    cmp al, 'r'
    je reboot
    cmp al, 's'
    je shutdown
    cmp al, 'g'
    je init_gui     ; Return to GUI mode
    cmp al, 0x0D    ; Enter key
    je text_command_loop

    ; Unknown command
    mov si, unknown_cmd
    call print_string_text
    jmp text_command_loop

; Display startup message in graphics mode
display_startup:
    push ax
    push bx
    push dx
    push si
    
    ; Display loading message
    mov ax, 10      ; X position
    mov bx, 25      ; Y position
    mov si, startup_msg
    mov dl, 15      ; White color
    call draw_text
    
    ; Small delay
    mov cx, 0xFFFF
startup_delay:
    loop startup_delay
    
    pop si
    pop dx
    pop bx
    pop ax
    ret

; Graphics Drawing Functions

; Draw filled rectangle
; AX = X, BX = Y, CX = Width, DX = Height, DL = Color
draw_filled_rect:
    push ax
    push bx
    push cx
    push dx
    push di
    push es
    
    mov di, 0xA000
    mov es, di
    
    mov di, bx      ; DI = Y coordinate
    imul di, 320    ; DI = Y * 320
    add di, ax      ; DI = Y * 320 + X
    
    push dx         ; Save height
    mov dh, dl      ; Color in DH
    pop dx
    
fill_row:
    push cx         ; Save width
    push di         ; Save start of row
fill_pixel:
    mov [es:di], dh ; Set pixel color
    inc di
    loop fill_pixel
    
    pop di          ; Restore start of row
    pop cx          ; Restore width
    add di, 320     ; Move to next row
    dec dx
    jnz fill_row
    
    pop es
    pop di
    pop dx
    pop cx
    pop bx
    pop ax
    ret

; Draw rectangle outline
; AX = X, BX = Y, CX = Width, DX = Height, DL = Color  
draw_rect:
    push ax
    push bx
    push cx
    push dx
    
    ; Draw top line
    call draw_horizontal_line
    
    ; Draw bottom line
    add bx, dx
    dec bx
    call draw_horizontal_line
    sub bx, dx
    inc bx
    
    ; Draw left line
    call draw_vertical_line
    
    ; Draw right line
    add ax, cx
    dec ax
    call draw_vertical_line
    
    pop dx
    pop cx
    pop bx
    pop ax
    ret

; Draw horizontal line
; AX = X, BX = Y, CX = Length, DL = Color
draw_horizontal_line:
    push di
    push es
    push cx
    
    mov di, 0xA000
    mov es, di
    mov di, bx
    imul di, 320
    add di, ax
    
draw_h_pixel:
    mov [es:di], dl
    inc di
    loop draw_h_pixel
    
    pop cx
    pop es
    pop di
    ret

; Draw vertical line  
; AX = X, BX = Y, DX = Length, DL = Color
draw_vertical_line:
    push di
    push es
    push dx
    
    mov di, 0xA000
    mov es, di
    mov di, bx
    imul di, 320
    add di, ax
    
draw_v_pixel:
    mov [es:di], dl
    add di, 320
    dec dx
    jnz draw_v_pixel
    
    pop dx
    pop es
    pop di
    ret

; Simple text drawing (8x8 character)
; AX = X, BX = Y, SI = String pointer, DL = Color
draw_text:
    push ax
    push bx
    push cx
    push si
    
draw_char_loop:
    lodsb           ; Load character
    test al, al
    jz draw_text_done
    
    ; Draw character (simplified - just draw colored blocks)
    push ax
    mov cx, 6       ; Character width
    mov dx, 8       ; Character height
    call draw_filled_rect
    add ax, 8       ; Move to next character position
    pop ax
    
    jmp draw_char_loop

draw_text_done:
    pop si
    pop cx
    pop bx
    pop ax
    ret

; Mouse Functions

; Initialize mouse driver
init_mouse:
    push ax
    
    ; Reset mouse
    mov ax, 0x00
    int 0x33
    
    ; Show mouse cursor
    mov ax, 0x01
    int 0x33
    
    ; Set mouse cursor to center of screen
    mov ax, 0x04
    mov cx, 160     ; X = 160 (center of 320)
    mov dx, 100     ; Y = 100 (center of 200)
    int 0x33
    
    pop ax
    ret

; Check mouse input
check_mouse:
    push ax
    push bx
    push cx
    push dx
    
    ; Get mouse status
    mov ax, 0x03
    int 0x33
    
    ; Check if left button pressed
    test bx, 0x01
    jz mouse_done
    
    ; Mouse clicked - check if clicked on close button
    cmp cx, 280     ; X >= 280
    jl mouse_done
    cmp cx, 295     ; X <= 295
    jg mouse_done
    cmp dx, 50      ; Y >= 50
    jl mouse_done
    cmp dx, 65      ; Y <= 65
    jg mouse_done
    
    ; Close button clicked - switch to text mode
    jmp text_mode

mouse_done:
    pop dx
    pop cx
    pop bx
    pop ax
    ret

; Text Mode Functions (for backward compatibility)

; Print character in AL (text mode)
print_char_text:
    push ax
    push bx
    mov ah, 0x0E
    mov bh, 0
    mov bl, 0x07
    int 0x10
    pop bx
    pop ax
    ret

; Print string pointed to by SI (text mode)
print_string_text:
    push ax
    push bx
    mov ah, 0x0E
    mov bh, 0
    mov bl, 0x0F    ; Bright white
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

; Read single character (text mode)
read_char_text:
    mov ah, 0x00
    int 0x16        ; BIOS keyboard interrupt
    ; Echo character
    call print_char_text
    ret

; Print newline (text mode)
newline_text:
    push ax
    mov al, 0x0D
    call print_char_text
    mov al, 0x0A
    call print_char_text
    pop ax
    ret

; System Functions

show_help:
    call newline_text
    mov si, help_text
    call print_string_text
    jmp text_command_loop

show_info:
    call newline_text
    mov si, info_text
    call print_string_text
    jmp text_command_loop

reboot:
    mov si, reboot_msg
    call print_string_text
    ; Reboot using keyboard controller
    mov al, 0xFE
    out 0x64, al
    hlt

shutdown:
    mov si, shutdown_msg
    call print_string_text
    ; Try VMware ACPI shutdown first
    mov ax, 0x2000
    mov dx, 0x604
    out dx, ax
    ; Try VirtualBox ACPI shutdown
    mov ax, 0x2000
    mov dx, 0x604
    out dx, ax
    hlt

; Messages and Data

; Graphics mode text
title_text      db 'Simple OS GUI - VMware & VirtualBox Ready', 0
startup_msg     db 'Initializing GUI Desktop...', 0
icon_text       db 'System', 0
start_text      db 'Start', 0
window_title    db 'System Information', 0
close_x         db 'X', 0

; System information for GUI window
sys_info1       db 'Architecture: x86 16-bit', 0
sys_info2       db 'Graphics: VGA 320x200x256', 0
sys_info3       db 'Keyboard: PS/2 supported', 0
sys_info4       db 'Mouse: PS/2 supported', 0
sys_info5       db 'VM: VMware & VirtualBox', 0

; Text mode messages  
text_mode_msg   db '==========================================', 0x0D, 0x0A
                db '    Simple OS - Text Mode Interface      ', 0x0D, 0x0A
                db '==========================================', 0x0D, 0x0A
                db 'Commands: h=help, i=info, r=reboot, s=shutdown, g=GUI', 0x0D, 0x0A
                db 'Press ESC in GUI mode to return to text mode', 0x0D, 0x0A, 0x0D, 0x0A, 0

prompt          db 'OS> ', 0

help_text       db 'Enhanced Simple OS Help:', 0x0D, 0x0A
                db 'This OS supports both text and GUI modes.', 0x0D, 0x0A
                db 'Commands:', 0x0D, 0x0A
                db '  h - Show this help', 0x0D, 0x0A
                db '  i - Show system information', 0x0D, 0x0A
                db '  g - Switch to GUI mode', 0x0D, 0x0A
                db '  r - Reboot system', 0x0D, 0x0A
                db '  s - Shutdown system', 0x0D, 0x0A
                db 'In GUI mode: ESC=text mode, Mouse=click', 0x0D, 0x0A, 0

info_text       db 'Enhanced System Information:', 0x0D, 0x0A
                db '- Status: Running in VMware/VirtualBox', 0x0D, 0x0A
                db '- Kernel loaded at 0x1000', 0x0D, 0x0A
                db '- Text mode: 80x25 VGA', 0x0D, 0x0A
                db '- Graphics mode: 320x200x256 VGA', 0x0D, 0x0A
                db '- Features: GUI desktop, mouse support', 0x0D, 0x0A
                db '- Input: PS/2 keyboard and mouse', 0x0D, 0x0A, 0

unknown_cmd     db ' - Unknown command (try h for help)', 0x0D, 0x0A, 0

reboot_msg      db 'Rebooting system...', 0x0D, 0x0A, 0
shutdown_msg    db 'Shutting down (VMware/VirtualBox compatible)...', 0x0D, 0x0A, 0

; Pad kernel to 4 sectors (2048 bytes) for enhanced functionality
times 2048-($-$$) db 0