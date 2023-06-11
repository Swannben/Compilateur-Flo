%include	"io.asm"
section	.bss
sinput:	resb	255	;reserve a 255 byte space in memory for the users input string
v$a:	resd	1
section	.text
global _start
_start:
	push	15		
	push	2		
	pop	ebx				 ; dépile la seconde operande dans ebx
	pop	eax				 ; dépile la permière operande dans eax
	div	ebx				 ; effectue l'opération eax%ebx et met le résultat dans eax
	push	ebx				 ; empile le résultat
	pop	eax		
	call	iprintLF		
	mov	eax,	1			 ; 1 est le code de SYS_EXIT
	int	0x80				 ; exit
