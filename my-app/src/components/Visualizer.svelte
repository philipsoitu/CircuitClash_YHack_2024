<script lang="ts">
	import { onMount } from 'svelte';

	export let width = 500;
	export let height = 500;
	export let shdl = '';

	let canvas: HTMLCanvasElement;
	let ctx: CanvasRenderingContext2D | null = null;

	onMount(() => {
		ctx = canvas.getContext('2d');

		draw();
	});

	function draw() {
		// drawGate('nand', 100, 100);
		drawWire(10, 400, 100, 450, "yo");

        alert(shdl)
	}

    //parser functions
    


	//helper render functions
	function drawGate(x: number, y: number, width: number = 100, height: number = 50, name: string) {
		if (ctx !== null) {
			ctx.beginPath();
			ctx.rect(x, y, width, height);
			ctx.stroke();

			ctx.font = '14px Arial';
			ctx.fillText(name, x + width / 2 - 15, y + height / 2 + 5);
		}
	}

	function drawWire(x0: number, y0: number, x1: number, y1: number, name: string = '') {
		if (ctx !== null) {
			const width = x1 - x0;

			//text
			ctx.font = '14px Arial';
			ctx.fillText(name, x0 + width/6 - 3, y0 - 3);

			//lines
			ctx.moveTo(x0, y0);
			ctx.lineTo(x0 + width / 3, y0);
			ctx.lineTo(x1 - width / 3, y1);
			ctx.lineTo(x1, y1);
			ctx.stroke();
		}
	}
</script>

<canvas {width} {height} bind:this={canvas} style="border:1px solid #000000;" />
