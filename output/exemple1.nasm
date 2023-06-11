%include	"io.asm"
section	.bss
sinput:	resb	255	;reserve a 255 byte space in memory for the users input string
v$a:	resd	1
section	.text
global _start
_start:
	push	3		
	push	5		
	push	2		
	pop	ebx				 ; dépile la seconde operande dans ebx
	pop	eax				 ; dépile la permière operande dans eax
	imul	ebx				 ; effectue l'opération eax*ebx et met le résultat dans eax
	push	eax				 ; empile le résultat
	pop	ebx				 ; dépile la seconde operande dans ebx
	pop	eax				 ; dépile la permière operande dans eax
	add	eax,	ebx			 ; effectue l'opération eax+ebx et met le résultat dans eax
	push	eax				 ; empile le résultat
	pop	eax		
	call	iprintLF		
	push	5		
