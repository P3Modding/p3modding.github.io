# Render All Ships Patch

## Summary
This patch modifies P3 to render all ships at sea, not just the up to two ships spotted by each player ship.

## Details
The first half of the `draw_spotted_ships` function at `004516B0` determines which ships should be rendered.
It produces three things of interest:
- the amount of ships that should be drawn
- an array of ship indexes that should be drawn
- an array of ship y coordinates

The rest of the function does not have to be modified.

## Patch
The following function `fixup_all_ships` takes pointers to the two arrays as an argument, and returns the amount of ships that should be drawn.
It only enqueues ships whose status is `0xf` (merchant vessel at sea) and `0x12` (AI pirate vessel).
```c
#include <stdint.h>
#define CLASS6_PTR 0x006DD7A0

inline void* get_ship_by_index(uint16_t index) {
    uint32_t ships_ptr =  *(uint32_t*) (CLASS6_PTR + 0x04);
    return (void*) ships_ptr + 0x180 * (uint32_t) index;
}

inline uint16_t get_ships_size() {
    return *(uint16_t*) (CLASS6_PTR + 0xf4);
}

inline uint16_t get_ship_status(void* ship) {
    return *(uint16_t*) (((uint32_t) ship) + 0x134);
}

inline uint16_t get_ship_y_high(void* ship) {
    return *(uint16_t*) (((uint32_t) ship) + 0x22);
}

uint32_t fixup_all_ships(uint32_t* spotted_y, uint32_t* spotted_index) {
    uint16_t ships_size = get_ships_size();
    int new_spotted_size = 0;

    for (uint16_t i = 0; i < ships_size; i++) {
        void* ship = get_ship_by_index(i);
        uint16_t status = get_ship_status(ship);

        if (status != 0x12 && status != 0xf) {
            continue;
        }

        spotted_y[new_spotted_size] = get_ship_y_high(ship);
        spotted_index[new_spotted_size] = i;

        new_spotted_size += 1;
    }

    return new_spotted_size;
}
```

Built with gcc 14.1 (`-m32 -O3 -fno-stack-protector`) this generates the following assembly:
```assembly
fixup_all_ships:
        push    ebp
        push    edi
        push    esi
        push    ebx
        movzx   ebx, WORD PTR ds:7198868
        mov     esi, DWORD PTR [esp+20]
        mov     edi, DWORD PTR [esp+24]
        test    bx, bx
        je      .L6
        xor     ecx, ecx
        xor     eax, eax
.L5:
        lea     edx, [ecx+ecx*2]
        sal     edx, 7
        add     edx, DWORD PTR ds:7198628
        movzx   ebp, WORD PTR [edx+308]
        cmp     bp, 18
        je      .L7
        cmp     bp, 15
        jne     .L3
.L7:
        movzx   edx, WORD PTR [edx+34]
        mov     DWORD PTR [esi+eax*4], edx
        mov     DWORD PTR [edi+eax*4], ecx
        add     eax, 1
.L3:
        add     ecx, 1
        cmp     ebx, ecx
        jne     .L5
        pop     ebx
        pop     esi
        pop     edi
        pop     ebp
        ret
.L6:
        pop     ebx
        xor     eax, eax
        pop     esi
        pop     edi
        pop     ebp
        ret
```

A call to `fixup_all_ships` has to be injected at `0x00451759` with the following assembly instructions.
#ADDRESSOFPATCH needs to be replaced with the address of `fixup_all_ships`.
```assembly
# save regs
push eax
push ecx
push edx

# call fixup_all_ships
mov eax, [esp+0x30]
mov ecx, [esp+0x2C]
push ecx
push eax
mov edx, #ADDRESSOFPATCH
call edx
mov ebp, eax
pop eax
pop eax

# restore regs
pop edx
pop ecx
pop eax

# jump to second part of draw_spotted_ships
mov eax, 0x00451B58
jmp eax
```
