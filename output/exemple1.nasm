%include	"io.asm"
section	.bss
sinput:	resb	255	;reserve a 255 byte space in memory for the users input string
v$a:	resd	1
section	.text
global _start
_start:
	push	1		
	pop	eax		
	call	iprintLF		
	l1:			
	push	1		
	pop	eax		
	cmp	eax,	1	
	jne	l2		
	push	2		
	pop	eax		
	call	iprintLF		
	jmp	l1		
	l2:			
	mov	eax,	1			 ; 1 est le code de SYS_EXIT
	int	0x80				 ; exit
