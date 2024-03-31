<script>
	import Visualizer from '../components/Visualizer.svelte';
	let text = `INPUT A
INPUT B
OUTPUT S
OUTPUT C
WIRE T1
WIRE T2

STARTGATE MYXOR INPUT X INPUT Y OUTPUT Z

    WIRE T1
    WIRE T2

    OR X Y T1
    AND X Y T2
    NOT T2 T2
    AND T1 T2 Z

ENDGATE

STARTGATE ADDER INPUT X INPUT Y OUTPUT Z OUTPUT I
    
    MYXOR X Y Z
    AND X Y I

ENDGATE

ADDER A B S C`;
</script>

<div class="mx-5 my-5">
	<Visualizer width={500} height={500} shdl={text} />
</div>
