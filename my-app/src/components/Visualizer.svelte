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
		if (ctx === null) {
			console.error('Failed to get 2D context for canvas.');
		} else {
			// Set line width
			ctx.lineWidth = 10;

			// Wall
			ctx.strokeRect(75, 140, 150, 110);

			// Door
			ctx.fillRect(130, 190, 40, 60);

			// Roof
			ctx.beginPath();
			ctx.moveTo(50, 140);
			ctx.lineTo(150, 60);
			ctx.lineTo(250, 140);
			ctx.closePath();
			ctx.stroke();

			ctx.font = '30px Arial';
			ctx.fillText(shdl, 10, 50);
		}
	}
</script>

<canvas {width} {height} bind:this={canvas} style="border:1px solid #000000;" />
