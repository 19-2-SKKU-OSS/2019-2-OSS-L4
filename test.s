	.text
main:
	add $t1, $zero, $zero
	sub $t0, $zero, $zero
	and $t0, $zero, $zero
	nor $t0, $zero, $zero
	or $t0, $zero, $zero
	sll $t0, $zero, $zero
	srl $t0, $zero, $zero
	slt $t0, $zero, $zero
	addi $t0, $zero, 0
	andi $t0, $zero, 0
	ori $t0, $zero, 0
	slti $t0, $zero, 0
	lui $3, 0x1000
	j L2 #394
	addi $2,$2,3
L2:
	jal funct1 #395
	addi $v0,$zero,10
syscall         # exit()
	

funct1:
	addi $v0,$zero,1
	jr $ra  #399
