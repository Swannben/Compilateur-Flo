%include	"io.asm"
section	.bss
sinput:	resb	255	;reserve a 255 byte space in memory for the users input string
v$a:	resd	1
section	.text
global _start
_start:
	push	5		
	push	10		
	pop	ebx				 ; dépile la seconde operande dans ebx
	pop	eax				 ; dépile la permière operande dans eax
	cmp	eax,	ebx			 ; on démarre la comparaison
	JE	L1				 ; si c'est vrai on saute à L1
	JLE	L2				 ; si c'est faux on saute à L2
	L1:	push,	1			 ; L1
	JMP	L3				 ; si c'est faux on saute à L2
	L2:	push,	00			 ; L2
	L3:			
	pop	eax		
	call	iprintLF		
	mov	eax,	1			 ; 1 est le code de SYS_EXIT
	int	0x80				 ; exit
